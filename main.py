from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/add-university', methods=['POST'])
def add_university():
    data = request.get_json()
    for uni in data.get('uczelnie', []):
        uni_key = f"university:{uni['name']}"
        redis_client.hset(uni_key, mapping={
            'type': uni.get('type', 'uczelnia'),
            'miasto': uni.get('miasto'),
            'score': uni.get('score', 0)
        })
    return jsonify(status='success', message='Universities added/updated successfully'), 200

if __name__ == '__main__':
    app.run(debug=True)
