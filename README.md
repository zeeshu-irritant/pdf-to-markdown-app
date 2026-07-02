# 📄 AI PDF-to-Markdown Workspace

An enterprise-grade document extraction utility built with Python and Streamlit. This application leverages IBM's open-source **Docling** (powered by DocLayNet) to convert PDF documents into clean, structurally accurate Markdown (`.md`) files. 

Unlike traditional heuristic PDF parsers, this tool utilizes deep learning to perfectly extract complex tables, preserve layouts, and securely embed high-resolution images directly into the Markdown code via Base64 encoding.

## ✨ Key Features

* **🧠 AI-Powered Layout Analysis:** Uses IBM Docling to accurately detect and extract text, lists, and complex table structures.
* **🖼️ Embedded Images:** Automatically extracts images from the PDF and embeds them directly into the Markdown file as Base64 strings. No need for external image folders or `.zip` archives.
* **👀 Real-Time Markdown Visualizer:** A built-in, side-by-side interactive auditor. Paste, edit, or upload Markdown code and see it render beautifully in real-time.
* **🔒 Privacy-First:** When run locally, all file processing happens directly on your machine.
* **📱 Responsive UI:** Built with Streamlit for a clean, modern, and accessible user experience.

## 🛠️ Prerequisites

Ensure you have the following installed on your system:
* Python 3.9 or higher
* `pip` (Python package installer)

## 🚀 Local Installation & Setup

Follow these steps to run the application on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/zeeshu-irritant/pdf-to-markdown-app.git
   cd pdf-to-markdown-app
   ```

2. **Install the required dependencies:**
   It is highly recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: The dependencies include `streamlit` and `docling`.)*

3. **Launch the application:**
   ```bash
   streamlit run app.py
   ```
   *Your default web browser will automatically open to `http://localhost:8501`.*

> **💡 Important Note on First Run:** The very first time you process a PDF, the application will download IBM's AI layout models (~1GB) to your local cache. This will take a few minutes depending on your internet speed. All subsequent conversions will be significantly faster.

## 💻 How to Use

The application is divided into two primary workspaces:

### Tab 1: Document Converter
1. Upload any standard `.pdf` document.
2. Click **Initialize Conversion**.
3. Once the AI finishes parsing, click the download button to save your self-contained `.md` file.

### Tab 2: Markdown Visualizer
1. Upload a `.md` file, or simply navigate to this tab after converting a document (it will auto-load your recent conversion).
2. Use the left panel to inspect or edit the raw Markdown source code.
3. Watch the right panel render your document, including tables and embedded images, in real-time.

## 🌐 Deployment (Streamlit Cloud / Hugging Face)

This application is fully ready to be deployed to the cloud so anyone can use it without installing Python.

1. Push this codebase to a public GitHub repository.
2. Log in to Streamlit Community Cloud (share.streamlit.io) or Hugging Face Spaces.
3. Connect your GitHub account and select this repository.
4. Set the main file path to `app.py`.
5. Deploy! The cloud environment will automatically install the libraries from `requirements.txt` and launch your app.

## 📜 License & Acknowledgements

* **Docling Engine:** Built utilizing IBM Docling.
* **UI Framework:** Built with Streamlit.
