import zmq
import time

context = zmq.Context()

subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://172.16.139.24:5556")
subscriber.connect("tcp://172.16.139.24:7721")
subscriber.setsockopt_string(zmq.SUBSCRIBE, "NASDAQ")

publisher = context.socket(zmq.PUB)
publisher.bind("ipc://nasdaq-feed")

while True:
    message = subscriber.recv()
    publisher.send(message)