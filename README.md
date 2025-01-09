 


# Raptor: Your Multimodal Chatbot ⚡️  

Raptor is an intelligent and multimodal chatbot built with Streamlit. It leverages Google's Gemini Flash model to provide real-time responses to both text and image inputs. The chatbot offers a personalized experience by recognizing and greeting users.  

## Features 🌟  

- **User Recognition**: Raptor greets the user by name, adding a personal touch to the experience.  
- **Multimodal Interaction**: Accepts both text and image inputs for richer context and interaction.  
- **Powerful AI**: Uses Google's Gemini Flash model to generate accurate and fast responses.  
- **Interactive Chat**: Maintains a conversation history for a seamless chat experience.  
- **Secure API Integration**: Ensures the user's API key remains private and protected.  

## Prerequisites  

- Python 3.8 or higher  
- Google AI Studio API Key  

## Installation 🛠️  

1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/shiwanshra1/raptor-multimodal-chatbot.git  
   cd raptor-multimodal-chatbot  
   ```  

2. **Install Dependencies**:  
   Use `pip` to install the necessary libraries:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Obtain an API Key**:  
   - Sign up for an [API Key from Google AI Studio](https://aistudio.google.com/app/apikey).  
   - Keep your API Key ready for use.  

## Usage 🚀  

1. **Run the Application**:  
   ```bash  
   streamlit run RaptorGemini.py  
   ```  

2. **Enter Your API Key**:  
   When prompted, provide your Google AI Studio API Key.  

3. **Start Chatting**:  
   - Upload an image (optional) to provide additional context.  
   - Enter your query in the chat box to receive instant responses from Raptor.  

## Example Usage 📝  

### Text Only:  
- Query: "What is the capital of France?"  
- Raptor’s Response: "The capital of France is Paris."  

### Image and Text:  
- Upload an image of a dog and ask: "What breed is this?"  
- Raptor will analyze the image and provide an appropriate response.  

## Project Structure 📂  

```
raptor-multimodal-chatbot/  
├── RaptorGemini.py         # Main application script  
├── requirements.txt        # List of required Python libraries  
├── README.md               # Project documentation  
```  

## Key Components 💡  

- **Streamlit Interface**: Provides an interactive and user-friendly UI.  
- **Gemini Flash Model**: Handles text and image processing with exceptional speed and accuracy.  
- **Chat History**: Displays the conversation in a clean and intuitive format.  

## Troubleshooting 🔧  

- **API Key Error**: Ensure your API key is valid and correctly entered.  
- **Image Upload Issue**: Verify the file format (JPG, JPEG, or PNG) and ensure the file is not corrupted.  
- **Dependencies**: If there are issues with libraries, run:  
  ```bash  
  pip install -r requirements.txt  
  ```  

## Acknowledgements  

- **Streamlit**: For the application framework.  
- **Google Generative AI**: For the Gemini Flash model.  

## Contributing 🤝  

Contributions are welcome! Fork the repository, make your improvements, and submit a pull request.  

## License  

This project is licensed under the MIT License.  

---

🚀 Developed with ❤️ by [Shiwansh Rai](https://github.com/shiwanshra1)  
```  

