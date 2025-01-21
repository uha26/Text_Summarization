import streamlit as st
from summarizer import summarize_text  # Import the summarization function

# Streamlit application layout
st.title("Text Summarizer")
st.header("Summarize Your Text")

# Text input area for the user
input_text = st.text_area("Enter your text here:")

# Button to trigger summarization
if st.button("Summarize"):
    if input_text.strip():
        summarized_text = summarize_text(input_text)
        st.subheader("Summarized Text:")
        st.write(summarized_text)
    else:
        st.warning("Please enter some text to summarize.")
