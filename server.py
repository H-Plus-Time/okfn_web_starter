import sys

from flask import Flask, send_from_directory, jsonify, request
app = Flask(__name__, static_folder='views')
from database import init_db, db_session, safe_add, result_to_json
from models import User

data = {
  "users": [
    {"name": "Mary Sue", "email": "mary.sue@example.com", "latitude": 144.96, "longitude": -37.800},
    {"name": "John Doe", "email": "john.doe@example.com", "latitude": 144.96, "longitude": -37.800},
    {"name": "John Smith", "email": "john.smith@example.com", "latitude": 144.96, "longitude": -37.800},
    {"name": "John Doe", "email": "john.doe@example.com", "latitude": 144.96, "longitude": -37.800},
    {"name": "John Doe", "email": "john.doe@example.com", "latitude": 144.96, "longitude": -37.800},
    {"name": "John Doe", "email": "john.doe@example.com", "latitude": 144.96, "longitude": -37.800},
    {"name": "John Doe", "email": "john.doe@example.com", "latitude": 144.96, "longitude": -37.800},
    {"name": "John Doe", "email": "john.doe@example.com", "latitude": 144.96, "longitude": -37.800},
    {"name": "John Doe", "email": "john.doe@example.com", "latitude": 144.96, "longitude": -37.800},
    {"name": "John Doe", "email": "john.doe@example.com", "latitude": 144.96, "longitude": -37.800},
  ]
}

init_db()
for user in data['users']:
  safe_add(User(user))
print >> sys.stderr, result_to_json(db_session.query(User).all())

@app.route("/")
def hello():
  return app.send_static_file('index.html')

@app.route("/chartjs")
def chartjs():
  return app.send_static_file("index-chartjs.html")

@app.route("/leafletjs")
def leafletjs():
  return app.send_static_file("index-leafletjs.html")
  
@app.route("/bower_components/<path:path>")
def bower(path):
  print(path)
  return send_from_directory('bower_components', path)
  
@app.route("/users", methods=["GET"])
def get_users():
  return jsonify({"users": result_to_json(db_session.query(User).all())})

@app.route("/users", methods=["POST"])
def add_user():
  safe_add[request.args['user']]
  return '"OK"'

@app.route('/<path:path>')
def send_static(path):
  return send_from_directory('public', path)

if __name__ == "__main__":
  # Remember to specify both host and port because HyperDev expects them
  print >> sys.stderr, 'Your app is listening on port 3000'
  app.run(host='0.0.0.0', port=3000, threaded=True)
