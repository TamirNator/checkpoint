#!flask/bin/python
from flask import Flask, request, jsonify

app = Flask(__name__)
counter = 0
getCounter = 0
@app.route('/', methods=["POST", "GET"])
def index():
    global counter
    global getCounter
    if request.method == "POST":
        counter+=1
        return "Hmm, Plus 1 please "
    else:
        getCounter+=1
        return str(f"Our counter is: {getCounter} ")
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200
if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')