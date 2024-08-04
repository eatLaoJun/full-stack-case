from flask import Flask, jsonify
from flask_cors import CORS

from dotenv import load_dotenv

import os
load_dotenv()

app = Flask(__name__)

CORS(app)


DATABASE_URL = os.getenv('DATABASE_URL', 'default_database_url2')
API_KEY = os.getenv('API_KEY', 'default_api_key')

@app.route('/api/hello')
def hello():
    return jsonify(message="Hello from Flask!")

@app.route('/status')
def hello_status():
    return jsonify(message="ok")

@app.route('/api/env')
def hello_env():
    return jsonify(message="Hello .env", api_key=API_KEY, database_url=DATABASE_URL)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3434)