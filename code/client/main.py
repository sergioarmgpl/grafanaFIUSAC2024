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
    team = random.randint(1,2)
    r.hincrby("teams","team"+str(team),1)
    r.incr("total",1)
    print({"team"+str(team):1},file=sys.stderr)
    sleep(0.3)
