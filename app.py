from pathlib import Path
import streamlit as st
from PIL import Image

# Path settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" /"main.css"
resume_file = current_dir / "assets" / "TK_Lebenslauf.pdf"
profile_pic = current_dir / "assets" / "tomkau.jpg"

# General settings
PAGE_TITLE = "Digital CV | Tom Kaufmann"
PAGE_ICON = ":infinity:"
NAME = "Tom Kaufmann"
DESCRIPTION ="""
Coder and skier from the heart of Europe.
"""
EMAIL = "th.kauf@web.de"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/thomas-kaufmann-ing",
    "GitHub": "https://github.com/tomkaufmann",
    "Twitter": "https://twitter.com/TomKaufm",
}
PROJECTS = {
    "Calculator for developing embedded systems": "https://apps.microsoft.com/detail/9mtxp4jz9n1n?activetab=pivot%3Aoverviewtab&hl=de-at&gl=AT",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Load css, pdf & profile picture
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Hero section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("Email:", EMAIL)

# Social links
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# Projects & Accomplishments
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
