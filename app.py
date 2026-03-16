from flask import Flask
import redis

app = Flask(__name__)

redis_client = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
        redis_client.incr('visits')
            visits = redis_client.get('visits').decode('utf-8')
                return f"Hello! You visited this page {visits} times."

            if __name__ == "__main__":
                    app.run(host="0.0.0.0", port=5000)
