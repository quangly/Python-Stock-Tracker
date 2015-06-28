"""
Server RESTful api
"""
import sys
sys.path.append(".")
sys.path.append("..")

from flask import Flask, jsonify, request, send_from_directory, render_template
import json

import logging
logger = logging.getLogger('webserver')

from App.common import logconfig
logconfig.load()

app = Flask("WebApp",
            template_folder='static/',
            static_folder='static',
            static_url_path='/static'
        )


@app.route("/")
def index():
    """
    notice: send_from_directory use current module's path as root_path to look for file
    no matter what work path you set for the web application.
    :return:
    """
    return send_from_directory('static/', filename="stocks.html")



@app.route("/test", methods=['GET'])
def getid():
    """
    Example: http://localhost:5555/test?id=2197447&type=mytype
    :return dictionary:
    """
    id = request.args.get("id")
    mytype = request.args.get("mytype")
    return jsonify({"id" : '123', "type":"mytypeABC"})


@app.route("/api/add", methods=['POST'])
def postid():
    """
    Usage: http://localhost:5555/api/postid
    httpmethod: POST
    Content-Type: application/json
    Raw Form Data: {"id": 1234}
    """
    data = json.loads(request.data)
    id = data["id"]   
    my_dict = {"id": str(id)}
    return jsonify(my_dict)

if __name__ == "__main__":
    app.run(host=None, port=5555, threaded=True, debug=True)