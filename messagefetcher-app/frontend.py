import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def display_value():
    try:
        # It calls the second container by its name 'backend-node'
        response = requests.get("http://backend-node:6000/get-value")
        secret_value = response.text
        return f"<h1>Container 1 (Frontend)</h1><p>Value fetched from Container 2: <b>{secret_value}</b></p>"
    except Exception as e:
        return f"Failed to reach the 2nd container: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
