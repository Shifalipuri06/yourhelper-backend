import streamlit as st

st.set_page_config(page_title="YourHelper", layout="centered")

st.title("📘 YourHelper")
st.subheader("Research Text & PDF Analysis")

st.write("Upload a PDF or paste text to analyze.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
text = st.text_area("Or paste text here", height=200)

if st.button("Analyze"):
    if uploaded_file:
        st.success("PDF uploaded successfully!")
        st.write("Analysis result will appear here.")
    elif text.strip():
        st.success("Text received!")
        st.write("Analysis result will appear here.")
    else:
        st.warning("Please upload a PDF or enter text.")
