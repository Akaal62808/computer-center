import streamlit as st

st.title("Contact Us")

name = st.text_input("Name")
phone = st.text_input("Phone")
message = st.text_area("Message")

if st.button("Send"):
    st.success("Message Sent Successfully!")

st.write("### Address")
st.write("Delhi, India")
