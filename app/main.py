from flask import Flask, jsonify
from config import load_config

config = load_config()

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from {config['app']['name']} running on {config['app']['env']}"

@app.route("/config")
def show_config():
    return jsonify(config)

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=config["app"]["port"])
    app.run(host=config["app"]["IPAddress"], port=config["app"]["port"])
