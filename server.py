from flask import Flask, jsonify
from flask import abort
from flask import request
from models.avm import AVM

app = Flask(__name__)
avm = AVM()

API_PATH = '/ml/api/'
API_VERSION = 'v1.0'
API_PREFIX = API_PATH + API_VERSION

@app.route(API_PATH + API_VERSION + '/price', methods=['POST'])
def price():
    data = {
        'bedrooms': 4,
        'bathrooms' :2.25,
        'sqft_living':2400,
        'sqft_lot':5350,
        'floors':1.5,
        'zipcode':98117
    }
    print(request.data)
    return str(avm.get_price(data))

@app.route('/')
def root():
  return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)