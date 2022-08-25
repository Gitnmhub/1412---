import redis
redis_cli = redis.StrictRedis(host='localhost', port=1412)
redis_cli.incr('test_count')