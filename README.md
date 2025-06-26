# data_compression-_and_decompression
# 🔐 File Compressor Web App

This is a simple yet powerful web application built with **Flask** that allows users to **compress** and **decompress** files using multiple algorithms like Huffman, LZ77, RLE, and built-in Python compressors (gzip, bz2, lzma, zlib).

---

## 📁 Project Structure
```
project_root/
│
├── app.py # Main Flask app with backend logic
├── utils/
│ └── compressors.py # Contains all compressor classes
├── templates/
│ └── index.html # Frontend HTML template
└── README.md # Project documentation (this file)
```

```ruby


---

## 🚀 Features

- 📤 Upload and compress any file
- 🧠 Auto-select best compression algorithm (based on result size)
- 🔄 Decompress previously compressed files
- 📦 Built-in support for multiple custom and standard algorithms
- 📊 Displays compression ratio, time taken, and file sizes
- 💡 Modern UI with simple and intuitive user interface
```
---

## 🧠 Supported Algorithms

| Algorithm | Type     | Description                                 |
|----------:|:--------:|---------------------------------------------|
| `auto`    | Smart    | Tries all and picks the best one            |
| `huffman` | Custom   | Huffman Encoding                            |
| `lz77`    | Custom   | LZ77 (Sliding Window Compression)           |
| `rle`     | Custom   | Run Length Encoding                         |
| `gzip`    | Built-in | Uses DEFLATE algorithm                      |
| `bz2`     | Built-in | Bzip2 compression                           |
| `lzma`    | Built-in | LZMA compression                            |
| `zlib`    | Built-in | Fast and effective compression              |

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd file_compression_decompression 
```
2. Set Up Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```
4. Install Dependencies
```bash
pip install flask flask-cors
```
or
```bash
pip install requirements.txt
```
5. Run the App
```
bash
python app.py
Visit the app at: http://127.0.0.1:5000
```

🌐 Web Interface
The UI provides:

File upload

Selection for operation (Compress/Decompress)

Algorithm selection (or Auto)

Result download

Status and info panel with metrics

📬 API Endpoints
POST /process
Handles both compression and decompression

Form Data:

file: File to upload

operation: "compress" or "decompress"

algorithm: (optional) "auto", "huffman", "lz77", etc.

GET /health
Returns:
```
json
{
  "status": "ok",
  "supported_algorithms": [...],
  "version": "5.0-refactored"
}
```
📄 Example Response
```
json
{
  "success": true,
  "operation": "compress",
  "algorithm": "huffman",
  "original_size": 2048,
  "processed_size": 832,
  "compression_ratio": 59.37,
  "processing_time": 0.016,
  "filename": "example_huffman.compressed",
  "file_data": [...]
}
```
👨‍💻 Author
Made with ❤️ by Umesh
Feel free to contribute or report issues.

