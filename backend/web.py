from flask import Flask, jsonify, render_template
import json
from datascraper import *



app = Flask(__name__)



@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api/v1/ticker=<ticker>')
def get_data(ticker):
    scraper = DataScraper(ticker)
    stock = scraper.get_ticker_obj()
    scraper.save_json()
    with open(f'data/{str(ticker)}_stock_info.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9080,debug=True)
