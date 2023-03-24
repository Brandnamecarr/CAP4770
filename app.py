'''
    File acts as the restAPI for the application.
'''
from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'message': 'Hello from the backend!'
    }
    return jsonify(data)

@app.route('/api/string', methods=['GET'])
def send_string():
    data = {
        'message': 'Brandon Carr'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
