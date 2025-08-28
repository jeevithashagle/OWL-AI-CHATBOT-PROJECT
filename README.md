# 🦉 Owl AI Chat

A beautiful AI chat interface powered by Google's Gemini API, built with Flask and modern CSS.

## Features

- ✨ Beautiful neon-themed UI with animations
- 🤖 Powered by Google Gemini 1.5 Flash
- 📱 Mobile-responsive design
- ⚡ Real-time chat interface
- 🔒 Secure API key management

## Setup Instructions

### 1. Get Your Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

**Option 1: Environment Variable (Recommended)**
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_api_key_here
```

**Option 2: Direct in Code**
Edit `app.py` and replace the API key in line 15:
```python
api_key = os.getenv('GEMINI_API_KEY', "your_api_key_here")
```

### 4. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## Project Structure

```
owl/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── templates/
│   └── index.html     # Chat interface
└── .env               # Environment variables (create this)
```

## Requirements

- Python 3.7+
- Flask
- google-generativeai
- python-dotenv

## Usage

1. Open your browser and go to `http://localhost:5000`
2. Type your question in the input field
3. Press Enter or click Send
4. Enjoy chatting with Owl AI! 🦉

## Troubleshooting

- **API Key Error**: Make sure your Gemini API key is valid and properly configured
- **Import Error**: Run `pip install -r requirements.txt` to install all dependencies
- **Port Already in Use**: Change the port in `app.py` or kill the process using port 5000

## Security Note

Never commit your API key to version control. Always use environment variables or `.env` files for sensitive information.
