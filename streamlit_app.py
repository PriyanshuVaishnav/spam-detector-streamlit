
import streamlit as st
from main import predict_spam

st.title("📩 Spam Message Detector")
st.write("Enter a message below to check whether it's spam or not.")

user_input = st.text_area("Message")

if st.button("Check"):
    if user_input.strip() == "":
        st.warning("Please enter a message to check.")
    else:
        result = predict_spam(user_input)
        if result == "Spam":
            st.error("🚨 This is likely SPAM!")
        else:
            st.success("✅ This is NOT spam.")
