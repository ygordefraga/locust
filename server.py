from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/delayed', methods=['GET'])
def delayed():
    time.sleep(1)
    return jsonify({'message': 'Delayed response'})

users = {
    1: {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'},
    2: {'name': 'Bob', 'age': 25, 'email': 'bob@example.com'},
    3: {'name': 'Charlie', 'age': 35, 'email': 'charlie@example.com'},
    4: {'name': 'David', 'age': 40, 'email': 'david@example.com'},
    5: {'name': 'Eve', 'age': 28, 'email': 'eve@example.com'}
}

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user_info = users.get(user_id)
    if user_info:
        return jsonify(user_info)
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/throw-exception', methods=['POST'])
def throw_exception():
    try:
        # Randomly throw an exception
        if random.random() < 0.5:
            raise Exception("Randomly generated exception")
        else:
            return jsonify({'message': 'No exception thrown'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)