# wattsapp

A faux-whatsapp interface to chat with AI Allan Watts. 
Flask-based, Ollama-served.

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running

1. Activate virtual environment (if not already activated)
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. Open your browser and navigate to `http://localhost:5000`

## Reqs

- Python 3.x
- Ollama (for AI chat capabilities)
- Dependencies listed in requirements.txt
