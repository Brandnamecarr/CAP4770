'''
    File acts as the restAPI for the application.
'''
from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import operations

app = Flask(__name__)
CORS(app)
OPS = operations()

@app.route('/api/data', methods=['GET'])
def get_data():
    myStr = OPS.apiTest()
    data = {
        'message': myStr
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
