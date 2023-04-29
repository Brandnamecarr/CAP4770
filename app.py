'''
    File acts as the restAPI for the application.
'''
from flask import Flask, jsonify, request
from flask_cors import CORS
import operations

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET', 'POST'])
def data():
    if request.method == 'GET':
        return get_data()
    elif request.method == 'POST':
        return post_data()

def get_data():
    # commented out for now due to error
    # myStr = OPS.apiTest()
    data = {
        'message': "getting data"
    }
    return jsonify(data)

def post_data():
    values = request.json
    #print(values)
    predicted_salary_value = operations.predict_salary(values)
    if predicted_salary_value == 'ERROR':
        data = {
            'status' : 'FAILURE',
            'message': 'error while making prediction',
            'predicted_salary': -1
        }
    else:
        data = {
            'status' : 'SUCCESS',
            'message': 'Data received',
            'predicted_salary': predicted_salary_value
        }
    print(data)
    return jsonify(data)

@app.route('/api/string', methods=['GET'])
def send_string():
    data = {
        'message': 'Brandon Carr'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)