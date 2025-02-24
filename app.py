from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
app = Flask(__name__, static_folder=".", static_url_path="")  # Serve static files

# Get the API key from environment variables
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/fix_code', methods=['POST'])
def fix_code():
    data = request.json
    user_code = data.get("code")

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Fix bugs in the following Python code:\n{user_code}")

    return jsonify({"fixed_code": response.text})

if __name__ == '__main__':
    app.run(debug=True)
