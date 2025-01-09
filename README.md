
# RAPTOR: Responsive Assistant for Personalised Tailored and Optimised Responses ⚡️

RAPTOR is an intelligent multimodal chatbot built using Streamlit. It integrates Google's Gemini Flash model to deliver lightning-fast, personalized responses to both text and image inputs. Designed with user recognition and interaction at its core, RAPTOR provides a tailored experience for every user.

## Features 🌟

- **Personalized User Recognition**: RAPTOR identifies and greets users by name for a unique interaction.  
- **Multimodal Inputs**: Accepts both text and image inputs to provide richer, contextual responses.  
- **Cutting-Edge AI**: Leverages Google's Gemini Flash model for accurate and fast conversational responses.  
- **Interactive Chat Interface**: Maintains conversation history for a seamless user experience.  
- **Secure API Integration**: Ensures that your API key remains confidential and protected.  

## Prerequisites  

- Python 3.8 or higher  
- Google AI Studio API Key  

## Installation 🛠️  

1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/shiwanshra1/RAPTOR.git  
   cd RAPTOR  
   ```  

2. **Install Dependencies**:  
   Install the required libraries using `pip`:  
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
   When prompted, input your Google AI Studio API Key.  

3. **Interact with RAPTOR**:  
   - Upload an image (optional) to enhance context.  
   - Enter your query in the chat box to get instant, optimized responses.  

## Example Usage 📝  

### Text Only:  
- Query: "What is the tallest mountain in the world?"  
- RAPTOR’s Response: "The tallest mountain in the world is Mount Everest."  

### Image and Text:  
- Upload an image of a cat and ask: "What breed is this cat?"  
- RAPTOR will analyze the image and provide an accurate response.  

## Project Structure 📂  

```
RAPTOR/  
├── RaptorGemini.py         # Main application script  
├── requirements.txt        # List of required Python libraries  
├── README.md               # Project documentation  
```  

## Key Components 💡  

- **Streamlit Interface**: Ensures an intuitive and interactive user interface.  
- **Gemini Flash Model**: Provides exceptional speed and accuracy for multimodal interactions.  
- **Chat History**: Displays ongoing conversations for easy tracking and context.  

## Troubleshooting 🔧  

- **API Key Issues**: Double-check your API key for correctness.  
- **Image Upload Errors**: Ensure the image file format is supported (JPG, JPEG, or PNG).  
- **Dependencies**: Run the following command to fix library issues:  
  ```bash  
  pip install -r requirements.txt  
  ```  

## Acknowledgements  

- **Streamlit**: For building the application framework.  
- **Google Generative AI**: For the Gemini Flash model powering RAPTOR.  

## Contributing 🤝  

Contributions are welcome! Fork the repository, enhance the code, and submit a pull request.  

## License  

This project is licensed under the MIT License.  

---

🚀 Developed with ❤️ by [Shiwansh Rai](https://github.com/shiwanshra1)  
```

