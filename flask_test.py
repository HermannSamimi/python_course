import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/vehicles')
def get_vehicles():
    api_url = "https://68376b322c55e01d1849cb71.mockapi.io/api/v1/vehicles"
    response = requests.get(api_url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": response.status_code, "message": response.text}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)