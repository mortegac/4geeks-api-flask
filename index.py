from flask import Flask, request, jsonify

app = Flask(__name__)
app.run(debug=True)

# GET
@app.route('/', methods=['GET'])
def home():
    return 'Bienvenidos a mi API'


@app.route('/api/users', methods=['GET'])
def get_users():
    response = { 'method': 'GET', 'message':'todo ok' }
    return jsonify(response)

@app.route('/api/users/<id>', methods=['GET'])
def get_user(id):
    response = { 'method': 'GET - ID' }
    return jsonify(response)


# POST
@app.route('/api/users', methods=['POST'])
def create_user():
    response = { 'method': 'POST' }
    return jsonify(response)

# PUT
@app.route('/api/users/<id>', methods=['PUT'])
def update_user(id):
    response = { 'method': 'PUT' }
    return jsonify(response)
    

# DELETE 
@app.route('/api/users/<id>', methods=['DELETE'])
def delete_user(id):
    response = { 'method': 'DELETE' }
    return jsonify(response)
    

app.run(host='0.0.0.0') 




