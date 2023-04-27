from flask import Flask, jsonify

app = Flask(__name__)

data = {"name": "John", "age": 30, "city": "New York"}

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)
