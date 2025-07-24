from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/price', methods=['POST'])
def get_price():
    data = request.json
    base_price = float(data['base_price'])
    demand_factor = random.uniform(0.9, 1.2)
    stock_factor = random.uniform(0.8, 1.1)
    dynamic_price = round(base_price * demand_factor * stock_factor, 2)
    return jsonify({'dynamic_price': dynamic_price})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
