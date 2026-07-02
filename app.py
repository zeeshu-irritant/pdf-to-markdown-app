import streamlit as st
import pymupdf4llm
import tempfile
import os

# Set page configuration for a modern look
st.set_page_config(
    page_title="PDF to Markdown Converter",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS to make it look extra clean and beautiful
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #4F46E5; color: white; }
    .stButton>button:hover { background-color: #4338CA; color: white; }
    h1 { color: #1E293B; font-weight: 700; }
    p { color: #475569; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.title("📄 PDF to Markdown Converter")
st.write("Convert your PDFs into clean, token-optimized Markdown (`.md`) format instantly. Perfect for feeding clean data into ChatGPT, Claude, or Gemini.")

st.divider()

# File Uploader component
uploaded_file = st.file_uploader("Drag and drop your PDF file here", type=["pdf"])

if uploaded_file is not None:
    # Display file details
    st.success(f"Successfully uploaded: **{uploaded_file.name}**")
    
    # Create a conversion button
    if st.button("🚀 Convert to Markdown"):
        with st.spinner("Processing document... This takes just a moment."):
            try:
                # Save uploaded file to a temporary location
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_file_path = tmp_file.name

                # Perform the conversion
                md_text = pymupdf4llm.to_markdown(tmp_file_path)

                # Clean up the temporary file
                os.unlink(tmp_file_path)

                # Success UI & Download Button
                st.balloons()
                st.success("Conversion Complete!")
                
                # Proved a download button for the converted file
                output_filename = uploaded_file.name.rsplit(".", 1)[0] + ".md"
                st.download_button(
                    label="📥 Download Markdown File",
                    data=md_text,
                    file_name=output_filename,
                    mime="text/markdown"
                )

                # Live Preview Area
                st.divider()
                st.subheader("👀 Preview Output")
                with st.expander("Click to expand and view the generated Markdown"):
                    st.code(md_text, language="markdown")

            except Exception as e:
                st.error(f"An error occurred during conversion: {e}")