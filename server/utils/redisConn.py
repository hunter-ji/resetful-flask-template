import redis
import json
from server import app


class RedisConn:

    def __init__(self):
        pool = redis.Redis(host = app.config['REDIS_HOSTNAME'], port = app.config['REDIS_PORT'])
        self.redis_conn = redis.Redis(connection_pool = pool)

    def set(self, key, value, ex = 604800):
        self.redis_conn.set(key, json.dumps(value), ex = ex)

    def get(self, key):
        value = self.redis_conn.get(key)
        try:
            return json.loads(value)
        except Exception as e:
            print('[redis error] ', e)
            return value

    def delete(self, key):
        self.redis_conn.delete(key)

    def incr(self, key):
        self.redis_conn.incr(key)

    def exits(self, key):
        return self.redis_conn.exists(key)


if __name__ == '__main__':
    red = RedisConn()
    # red.set('hello', 'world')
    red.delete('hello')
