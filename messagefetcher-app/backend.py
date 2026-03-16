from flask import Flask

app = Flask(__name__)

@app.route('/get-value')
def provide_value():
    # This is the "Value" held in the 2nd container
    return "Hello from the Secret Backend Container!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
