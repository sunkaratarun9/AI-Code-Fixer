# AI Code Fixer

## 📌 Project Overview
AI Code Fixer is a simple web-based tool that helps developers find and fix errors in their code using AI. It provides a user-friendly interface, AI-powered corrections, and dark mode support.

## 🎯 Features
- **Easy-to-Use Interface** – Clean and responsive design.
- **Code Input & Output** – Paste code and get AI-generated fixes.
- **AI-Powered Corrections** – Uses Google Gemini API (or any LLM API) for code fixes.
- **Dark Mode Support** – Toggle between light and dark mode.
- **Copy to Clipboard** – Quickly copy the corrected code.

## 🔧 Technologies Used
- **Flask** – Backend framework for handling requests.
- **Google Generative AI** – AI-powered code corrections.
- **HTML** – Structure of the webpage.
- **CSS (Tailwind CSS)** – Styling for a modern and responsive UI.
- **JavaScript** – Handles user interactions.

## 📋 Requirements
### **Software Requirements**
- **Code Editor** – VS Code, Sublime Text, or any preferred editor.
- **Web Browser** – Chrome, Firefox, or Edge for testing.
- **API Access** – Google Generative AI API.

### **Technical Skills Required**
- **Python & Flask** – To set up the backend.
- **HTML & CSS** – To design the webpage.
- **JavaScript** – For handling interactions and API calls.

### **Hardware Requirements**
- **Basic PC/Laptop** – Minimum 4GB RAM, 64-bit OS.
- **Internet Connection** – Required for API calls.

## 🚀 How to Run the Project
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd AI-Code-Fixer
   ```
2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Up API Key**
   - Get an API key from Google Generative AI.
   - Store it in a `.env` file or directly in the script.
5. **Run the Flask Server**
   ```bash
   python app.py
   ```
6. **Open in Browser**
   - Go to `http://127.0.0.1:5000` to access the web app.

## 🔮 Future Enhancements
- **Support More Languages** – Python, Java, C++, etc.
- **Syntax Highlighting** – Better readability with CodeMirror.js.
- **Auto-Suggestions** – Real-time suggestions while typing.
- **Offline Mode** – Basic code fixes without an internet connection.
- **Save Code History** – Users can store and revisit previous fixes.

## 📌 Conclusion
AI Code Fixer makes coding easier by quickly identifying and fixing errors. With a clean design, AI-powered fixes, and planned future improvements, it’s a great tool for developers. 🚀
