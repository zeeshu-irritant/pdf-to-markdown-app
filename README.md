# 📄 PDF to Markdown Converter

A beautiful, lightweight, and user-friendly web application designed to convert PDF documents into clean, LLM-optimized Markdown (`.md`) files. Perfect for reducing token usage when working with AI models like Claude, ChatGPT, and Gemini.

Built using **Streamlit** and **PyMuPDF4LLM**.

## 🚀 Features
- **Drag-and-Drop Interface:** Easily upload any standard PDF document.
- **Token-Optimized Output:** Cleans away visual headers, footers, and page numbers while preserving structural lists, headings, and markdown tables.
- **Instant Preview:** View the converted markdown text right inside your browser before downloading.
- **Privacy First:** If run locally, files never leave your computer.

## 🛠️ Local Installation & Setup

If you want to run this application locally on your computer, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/zeeshu-irritant/pdf-to-markdown-app.git](https://github.com/zeeshu-irritant/pdf-to-markdown-app.git)
   cd pdf-to-markdown-app
   ```
   1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
   Your browser should automatically open to http://localhost:8501.
---

### 🌐 How to make it accessible to non-programmer friends

To share this app without forcing your friends to use GitHub, terminals, or Python, deploy it to the web for free:

1. Push this code to a public repository on your **GitHub** account.
2. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
3. Click **"New app"**, select your repository, select the `main` branch, and set the main file path to `app.py`.
4. Click **"Deploy!"**

Within a couple of minutes, Streamlit will give you a public URL (e.g., `https://your-app-name.streamlit.app/`). Anyone you share that link with can instantly convert their PDFs right from their web browser or phone!

Would you like to add any extra features to this setup, such as a feature to handle scanned PDFs via Optical Character Recognition (OCR)?