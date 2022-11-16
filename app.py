from pathlib import Path
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


# --- Website Title ---
st.set_page_config(
        page_title="My Protfolio",
        page_icon=":sunny:",
        layout="wide",
)


# --- Path Settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "static" / "style.css"
resume_file = current_dir / "static" / "resume.pdf"
profile_pic = current_dir / "static" / "family_bythesea.jpg"
map_pic = current_dir / "static" / "Self-Learning_Map.jpg"

# --- General Settings ---
PAGE_TITLE = "Portfolio"
PAGE_ICON = ":wave:"
NAME = "JainWha Huang"
DESCRIPTION = """
    I am Passionate about Learning and Sharing.
"""
EMAIL = "ericarthuang2021@gmail.com"
SOCAIL_MEDIA = {
    "GitHub": "https://github.com/ericarthuang",
    "YouTube": "https://www.facebook.com/ericarthuang",
    "Linkedin": "https://www.linkedin.com/in/%E5%BB%BA%E6%A8%BA-%E9%BB%83-57a3b4257/",
    "FB": "https://www.facebook.com/ericarthuang",
    "Twitter": "https://twitter.com/hungjinhu19",
}


# --- Load CSS, PDF, Profile Picture, Animation Assets ---
with open(css_file) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True,
    )

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

img_learning_map = Image.open(map_pic)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_animation = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_rnpgzd17.json")




# --- Header Section ---
st.title("Copy Learning in Computer Science")

with st.container():
    right_column, left_column = st.columns((2, 3))
    with right_column:
        st.image(profile_pic, width=420)
    with left_column:
        st.subheader(f"Hi, I am {NAME} :penguin:")
        st.write("I am Passionate about Learning and Sharing.")
        st.download_button(
            label="Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write(":e-mail:", EMAIL)
        st_lottie(
            lottie_animation, 
            height=150, 
            key="learning",
        )


# --- Social Link ---
cols = st.columns(len(SOCAIL_MEDIA))
for index, (platform, link) in enumerate(SOCAIL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- Main Section ---
with st.container():
    st.write("---")
    st.header("What I Learn")
    st.markdown("[:earth_asia:Welcome to My Copy Learning Website to Find the Memos and Projects](https://ericarthuang.github.io/My_Copy_Learning/)")
    
    left_column, right_column = st.columns((1, 2))
    with left_column:
        st.image(img_learning_map, width =400)
    with right_column:
        st.write("""
            - C, C++, Python, Data Structure and Algorithm
            - Machine Learning: Scilit-Learn, TensorFlow, Pytorch, and Computer Vision
            - Data Analysis: Numpy, Pandas, Web Scraping, and Power BI 
            - Data Visulization: Matplotlib, Seaborn, and Plotly
            - Web Application: Django, Flask, FastAPI, HTML, CSS, JavaScript, React, Node, and Express
            - Database and Cloud: MySQL, Postgres, and AWS
            - CI/CD: Github Version Control, GitHub Actions, and Doccker Deployment
            - Gaming: Pygame
            - Computer Architecture, Computer Organiztion, Networking, CyberSecurity, and Opeation System
            """
        ) 


# --- CONTACT ---
with st.container():
    st.write("---")
    st.header("Get in Touch")
    
    contact_form = """
    <form action="https://formsubmit.co/ericarthuang2021@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your Massages..."></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()