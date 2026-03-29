import streamlit as st

st.set_page_config(page_title="Sample Computer Centre", layout="wide")

st.markdown("""
<style>
.hero {
    background: linear-gradient(rgba(0,0,50,0.7), rgba(0,0,50,0.7)),
                url("https://cdn.pixabay.com/photo/2015/01/08/18/25/startup-593341_1280.jpg");
    background-size: cover;
    padding: 100px;
    text-align: center;
    color: white;
}
.btn {
    background: #00c6ff;
    padding: 10px 20px;
    color: white;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>Welcome to Sample Computer Centre</h1>
<p>You can develop your skills here</p>
<a href="#" class="btn">Join Now</a>
</div>
""", unsafe_allow_html=True)

st.write("## Our Top Courses")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/5968/5968350.png")
    st.write("Python")

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/2721/2721620.png")
    st.write("Web Development")

with col3:
    st.image("https://cdn-icons-png.flaticon.com/512/1055/1055687.png")
    st.write("Basic Computer")
