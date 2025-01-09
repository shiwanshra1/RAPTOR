import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Setting up the Streamlit application layout
st.set_page_config(page_title="Raptor: Your Multimodal Chatbot", layout="wide")
st.title("Welcome to Raptor, a Responsive Assistant for Personalized Tailored and Optimized Responses")
st.caption("You can ask me anything you want and keep a dip into the world of endless possibilities, Just dont ask me to take you to jurrasic")

# Recognize the user
USER_NAME = "Shiwansh Rai"  # Replace with your name or dynamically fetch it if needed
st.write(f"Hello, {USER_NAME}! Raptor is here to assist you.")
st.write("Feel free to upload an image and type in your queries to experience the magic of AI.")
st.write("Let's get started by entering your API key and uploading an image if you'd like.")

# Taking the API Key as input from the user
st.subheader("Step 1: Enter Your API Key")
st.write("To access the Gemini Flash model, please provide your Google API Key.")
st.write("Don't worry; your key will remain private and secure.")
api_key = st.text_input("Enter your Google API Key here:", type="password")

# Validate API key
if not api_key:
    st.warning("API Key is required to proceed.")
else:
    try:
        st.write("Configuring the Gemini Flash model...")
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
        st.success("API Key validated successfully! The model is ready to use.")
    except Exception as e:
        st.error(f"There was an error setting up the model: {e}")
        st.stop()

# Uploading an image
st.subheader("Step 2: Upload an Image (Optional)")
st.write("You can upload an image to provide additional context to your queries. Supported formats: JPG, JPEG, PNG.")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    try:
        st.write("Processing the uploaded image...")
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.success("Image uploaded successfully!")
    except Exception as e:
        st.error(f"There was an issue processing the image: {e}")

# Initializing chat history
st.subheader("Step 3: Start Chatting")
if "messages" not in st.session_state:
    st.session_state.messages = []

st.write("Type your query in the chat box below and receive responses instantly!")

# Displaying chat history
chat_placeholder = st.container()
with chat_placeholder:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Handling user input
st.write("You can ask anything. The model will try its best to answer using the provided inputs.")
prompt = st.chat_input("What do you want to know?")

if prompt:
    st.write("Processing your query...")
    inputs = [prompt]
    st.session_state.messages.append({"role": "user", "content": prompt})
    with chat_placeholder:
        with st.chat_message("user"):
            st.markdown(prompt)

    if uploaded_file:
        inputs.append(image)

    try:
        with st.spinner(f"Generating response from Raptor, your personal assistant..."):
            response = model.generate_content(inputs)

        # Save assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response.text})

        with chat_placeholder:
            with st.chat_message("assistant"):
                st.markdown(response.text)

    except Exception as e:
        st.error(f"An error occurred while generating the response: {e}")

# Handling scenarios where only an image is uploaded
if uploaded_file and not prompt:
    st.warning("Please enter a text query to accompany the uploaded image.")

# Footer with additional information
st.divider()
st.write("---")
