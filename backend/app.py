from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)

CORS(app)

@app.route('/api/hello')
def hello():
    return jsonify(message="Hello from Flask!")

@app.route('/status')
def hello_status():
    return jsonify(message="ok")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3434)