from flask import Flask, jsonify
import json

app = Flask(__name__)



@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/data')
def get_data():

    # Stock info ladem
    with open('data/stock_info.json') as f:
        data = json.load(f)
        
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)
