import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")
while True:
    data = input("input your data:")
    print(data)
    socket.send_string(data)