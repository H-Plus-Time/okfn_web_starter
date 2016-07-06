import sys

from flask import Flask, send_from_directory, jsonify, request
app = Flask(__name__, static_folder='views')

data = {
  "dreams": [
    "Find and count some sheep",
    "Climb a really tall mountain",
    "Wash the dishes"
  ]
}

@app.route("/")
def hello():
  return app.send_static_file('index.html')
  
@app.route("/poba")
def poba():
  return '"POBA"'
  
@app.route("/dreams", methods=["GET"])
def get_dreams():
  return jsonify(**data)

@app.route("/dreams", methods=["POST"])
def add_dream():
  data["dreams"].append(request.args["dream"])
  return '"OK"'

@app.route('/<path:path>')
def send_static(path):
  return send_from_directory('public', path)

if __name__ == "__main__":
  # Remember to specify both host and port because HyperDev expects them
  print >> sys.stderr, 'Your app is listening on port 3000'
  app.run(host='0.0.0.0', port=3000, threaded=True)
