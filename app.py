from urllib.parse import urlparse
from flask import request
from flask import jsonify
from flask import Flask

from flask import json
import datetime
import logging
import flask




app = Flask(__name__)

@app.route('/', methods=["GET"])
def returnjson():
    return jsonify({"timestamp": datetime.datetime.now(),"hostname": urlparse(request.base_url),"engine": flask.__version__, "visitors_ip": request.remote_addr}),200
    


if __name__ == "__main__":
    ## stream logs to a file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)

    app.run(host='0.0.0.0')
