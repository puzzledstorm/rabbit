import zmq

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind('tcp://*:5557')
while True:
    data = input("input your data:")
    socket.send_string(data)