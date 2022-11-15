from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(
        page_title="My Protfolio",
        page_icon=":sunny:",
        layout="wide",
)


# --- Use Local CSS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("./static/style.css")

# --- Load Animation Assets ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_animation = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_rnpgzd17.json")

img_learning_map = Image.open("./static/Self-Learning_Map.jpg")

# --- Header Section --
st.title("Copy Learning in Computer Science")

with st.container():
    st.subheader("Hi, I am JainWha Huang :penguin:")
    st.write("I am passionate aobut learning and sharing.")
    

# --- Main Section ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns((2, 3))
    with left_column:
        st_lottie(
            lottie_animation, 
            height=300, 
            key="learning",
        )
    with right_column:
        st.header("What I Learn")
        st.write("""
            - Computer Languages: C, C++, Python
            - Data Structure and Algorithm
            - Machine Learning: Scilit-Learn, TensorFlow, Pytorch, and Computer Vision
            - Data Analysis: Numpy, Pandas, Power BI, and Scraping
            - Data Visulizaion: Matplotlib, Seaborn, and Plotly
            - Web Application - HTML, CSS, JavaScript, React, Django, Flask, FastAPI, Node, and Express, MySQL, Postgres, and AWS
            - Github Version Control, GitHub Actions, and Doccker Deployment
            - Gaming: Pygame
            """
        )

    

# --- Memos and PROJECTS ---
with st.container():
    st.write("---")
    st.header("My Self-Learning Map")
    st.markdown("[:earth_asia:Welcome to My Copy Learning Website](https://ericarthuang.github.io/My_Copy_Learning/)")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_learning_map)
    with text_column:
        st.subheader("Starting Learning Coumputr Science from 54 Years Old.")
        st.write("Find Memos and Projects about My Self-learning Map.")
        st.write("Share Your Creatiive Thinking")
        

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