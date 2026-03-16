import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def display():
    try:
        # Calls the backend service
        response = requests.get("http://backend-service:6000/data")
        # This will show up in your browser
        return f"<h1>Frontend (Container 1)</h1><p>Data from Backend: <b>{response.text}</b></p>"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
