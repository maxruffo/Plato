from flask import Flask, jsonify, render_template
import json
import os.path
from datascraper import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'BACKEND!!!'

@app.route('/api/v1/ticker=<ticker>')
def get_data(ticker):
    json_path = f'data/stock_info/{str(ticker)}_stock_info.json'
    if not os.path.isfile(json_path):
        scraper = DataScraper(ticker)
        stock = scraper.get_ticker_obj()
        if stock is None:
            return jsonify({'error': f'Ticker {ticker} not found'})
        scraper.save_json()
    with open(json_path) as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9080, debug=True)
