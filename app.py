from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from CI/CD Pipeline 🚀",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENV", "dev")
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "UP"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)