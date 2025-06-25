from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os, base64, time, json
from utils.compressors import BuiltInCompressor, HuffmanCompressor, LZ77Compressor, RLECompressor, CompressorFactory

app = Flask(__name__, template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')))
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def handle_file():
    uploaded_file = request.files.get('file')
    if not uploaded_file or uploaded_file.filename == '':
        return jsonify({'success': False, 'error': 'No file uploaded'}), 400

    try:
        raw_data = uploaded_file.read()
        operation = request.form.get('operation')
        algorithm = request.form.get('algorithm', 'auto').lower()
        filename = uploaded_file.filename
        original_size = len(raw_data)

        if operation == 'compress':
            chosen_algorithms = [algorithm] if algorithm != 'auto' else CompressorFactory.get_all()
            for algo in chosen_algorithms:
                try:
                    compressor = CompressorFactory.get(algo)
                    start = time.time()
                    result = compressor.compress(raw_data)
                    compressed_data, metadata = result if isinstance(result, tuple) else (result, {})
                    duration = round(time.time() - start, 3)

                    if len(compressed_data) >= original_size:
                        continue

                    response_payload = {
                        'compressed_data': base64.b64encode(compressed_data).decode(),
                        'metadata': metadata,
                        'algorithm': algo,
                        'original_filename': filename
                    }

                    return jsonify({
                        'success': True,
                        'operation': 'compress',
                        'algorithm': algo,
                        'original_size': original_size,
                        'processed_size': len(compressed_data),
                        'compression_ratio': round((original_size - len(compressed_data)) / original_size * 100, 2),
                        'processing_time': duration,
                        'filename': f"{os.path.splitext(filename)[0]}_{algo}.compressed",
                        'file_data': list(json.dumps(response_payload).encode())
                    })

                except Exception:
                    continue

            return jsonify({'success': False, 'error': 'No compression succeeded'}), 400

        elif operation == 'decompress':
            parsed_payload = json.loads(raw_data.decode())
            compressed = base64.b64decode(parsed_payload['compressed_data'])
            meta = parsed_payload.get('metadata', {})
            algo = parsed_payload['algorithm']
            filename = parsed_payload['original_filename']
            decompressor = CompressorFactory.get(algo)
            start = time.time()
            output_data = decompressor.decompress(compressed, meta)
            duration = round(time.time() - start, 3)

            return jsonify({
                'success': True,
                'operation': 'decompress',
                'algorithm': algo,
                'original_size': len(compressed),
                'processed_size': len(output_data),
                'processing_time': duration,
                'filename': filename,
                'file_data': list(output_data)
            })

        return jsonify({'success': False, 'error': 'Unknown operation'}), 400

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'ok',
        'supported_algorithms': CompressorFactory.get_all(),
        'version': '5.0-refactored'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
