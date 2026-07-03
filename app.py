import streamlit as st
import tempfile
import os

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling_core.types.doc import ImageRefMode
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, TesseractCliOcrOptions

# Set Page Configuration
st.set_page_config(
    page_title="PDF to Markdown Converter",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject CSS for Premium Glassmorphism Styling
st.markdown("""
    <style>
    /* Modern Dark Gradient Background for the entire app */
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: #ffffff;
    }
    
    /* Frosted Glass effect for the main container */
    [data-testid="block-container"] {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 3rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        margin-top: 2rem;
        margin-bottom: 2rem;
    }
    
    /* Premium Styling for Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background-color: rgba(0, 0, 0, 0.2);
        border-radius: 12px;
        padding: 5px;
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 16px; 
        font-weight: 600; 
        padding: 10px 20px; 
        border-radius: 8px;
        color: #a1a1aa;
        background-color: transparent;
        border: none;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(255, 255, 255, 0.15);
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    /* Glassmorphic Buttons with Hover Animations */
    .stButton>button {
        width: 100%; 
        border-radius: 10px; 
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white; 
        font-weight: 600; 
        height: 45px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: rgba(255, 255, 255, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.4);
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        color: white;
    }
    
    /* Transparent input fields and file uploaders */
    [data-testid="stFileUploadDropzone"], .stTextArea textarea {
        background-color: rgba(0, 0, 0, 0.2) !important;
        border: 1px dashed rgba(255, 255, 255, 0.3) !important;
        color: white !important;
        border-radius: 12px;
    }
    
    /* Force text colors to contrast against the dark background */
    h1, h2, h3, p, label, .stMarkdown {
        color: #f8fafc !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("PDF to Markdown Conversion Workspace")
st.write("Enterprise-grade document extraction utilizing IBM DocLayNet. This utility converts PDF documents into structured Markdown while preserving layouts, tables, and embedding images.")
st.divider()

tab_convert, tab_visualize = st.tabs(["Document Converter", "Markdown Visualizer"])

# =====================================================================
# TAB 1: CONVERTER
# =====================================================================
with tab_convert:
    st.header("Upload and Convert Document")
    
    pdf_file = st.file_uploader("Select a PDF document for processing", type=["pdf"], key="pdf_uploader")
    
    if pdf_file is not None:
        if st.button("Initialize Conversion"):
            with st.spinner("Processing document layout and extracting structural elements..."):
                try:
                    with tempfile.TemporaryDirectory() as tmpdir:
                        pdf_path = os.path.join(tmpdir, "input.pdf")
                        
                        with open(pdf_path, "wb") as f:
                            f.write(pdf_file.getvalue())
                        
                        pipeline_options = PdfPipelineOptions()
                        pipeline_options.generate_picture_images = True 

                        # Tell Docling to use Tesseract OCR to bypass the RapidOCR read-only bug
                        pipeline_options.ocr_options = TesseractCliOcrOptions()
                        
                        converter = DocumentConverter(
                            format_options={
                                InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
                            }
                        )
                        
                        result = converter.convert(pdf_path)
                        md_text = result.document.export_to_markdown(image_mode=ImageRefMode.EMBEDDED)
                        
                        st.session_state['generated_md'] = md_text
                        st.success("Document conversion completed successfully. Images and tables are embedded.")
                        
                        base_name = pdf_file.name.rsplit(".", 1)[0]
                        st.download_button(
                            label="Download Markdown File (.md)",
                            data=md_text,
                            file_name=f"{base_name}.md",
                            mime="text/markdown"
                        )
                except Exception as e:
                    st.error(f"An error occurred during conversion: {e}")

# =====================================================================
# TAB 2: VISUALIZER (INTERACTIVE EDITING)
# =====================================================================
with tab_visualize:
    st.header("Markdown Validation and Preview")
    st.write("Review, edit, or paste Markdown structures directly to audit the rendered output in real-time.")
    
    # Initialize session state for the text editor if it doesn't exist
    if 'editor_content' not in st.session_state:
        st.session_state['editor_content'] = ""

    md_upload = st.file_uploader("Select a Markdown (.md) file to preview", type=["md"], key="md_uploader")
    
    # Button to explicitly load the file content into the text area
    if st.button("📥 Load File Content into Editor"):
        if md_upload is not None:
            st.session_state['editor_content'] = md_upload.getvalue().decode('utf-8')
            st.success("Uploaded file content loaded!")
        elif 'generated_md' in st.session_state:
            st.session_state['editor_content'] = st.session_state['generated_md']
            st.success("Loaded the most recently converted document!")
        else:
            st.warning("Please upload a .md file or convert a PDF first.")
        
    st.divider()
    col_raw, col_rendered = st.columns(2)
    
    with col_raw:
        st.subheader("Raw Markdown Output")
        
        # Binding the text area directly to the session state key "editor_content"
        st.text_area(
            "Source Code", 
            height=535, 
            label_visibility="collapsed",
            key="editor_content"
        )
        
        # A button to force Streamlit to refresh the UI and render the latest typed text
        st.button("🔄 Render / Update Visualization")
        
    with col_rendered:
        st.subheader("Rendered Document")
        with st.container(height=600, border=True):
            # Render whatever is currently stored in the session state
            if st.session_state['editor_content']:
                st.markdown(st.session_state['editor_content'])
