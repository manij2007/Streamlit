# 📂 Metadata Extractor with Streamlit

A simple and interactive **file metadata extraction application** built with **Streamlit**.  
This project allows users to upload different types of files, inspect their information, extract useful metadata, and monitor uploaded files through a simple analytics dashboard.

## 🚀 Features

### 🖼️ Image Metadata
- Upload `PNG`, `JPG`, and `JPEG` images
- Preview uploaded images
- Display basic file information
- Extract image metadata including:
  - Format
  - Format description
  - Dimensions
  - Width and height
  - Additional image information

### 🎵 Audio Files
- Upload `MP3`, `OGG`, and `WAV` files
- Play uploaded audio directly inside the application
- Display filename, file type, and file size

### 📄 PDF Documents
- Upload PDF documents
- Display basic file information
- Read and extract text from the first page using **PyPDF2**

### 📊 Analytics & Monitoring
Uploaded file information is stored in a local **SQLite database**.

The Analytics section provides:
- A table containing uploaded file records
- Filename, file type, file size, and upload time
- File type distribution visualization

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Pillow (PIL)
- PyPDF2
- SQLite
- Matplotlib
- Seaborn

## ▶️ Run the Project

Install the required dependencies:

```bash
pip install streamlit pandas pillow PyPDF2 matplotlib seaborn
```

Then start the Streamlit application:

```bash
streamlit run app.py
```

The application will automatically open in your browser.

## 📁 Project Structure

```text
Streamlit-Metadata-Extractor/
│
├── app.py
├── Database.db
└── README.md
```

## 🎯 Project Purpose

This project demonstrates how **Streamlit can be used to build interactive Python web applications** for file processing, metadata extraction, database storage, and simple data visualization.

It is a practical example of combining Python libraries with an easy-to-use web interface.
