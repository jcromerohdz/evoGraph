import os
import redis

REDISTOGO_URL =os.environ['REDISTOGO_URL']
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)