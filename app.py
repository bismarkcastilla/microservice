from datetime import datetime
from flask import Flask, jsonify, request
import socket
import sys


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    data = {
    "timestamp": datetime.now(),
    "hostname": socket.gethostname(),
    "engine": sys.version,
    "visitor ip": request.remote_addr
    }
        
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug = True)
