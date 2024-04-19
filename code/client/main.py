import os
import sys
from time import sleep
import random
import redis

rhost = os.environ['REDIS_HOST']
rauth = os.environ['REDIS_AUTH']
r = redis.StrictRedis(host=rhost,\
        port=6379,db=0,password=rauth,\
        decode_responses=True)

while True:
    d = random.randint(0,9)
    r.set("data",d)
    print({"data":d},file=sys.stderr)
    sleep(0.5)
