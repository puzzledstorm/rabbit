import zmq, sys

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
while True:
    data = input("input your data:")
    if data == 'q':
        sys.exit()
    socket.send_string(data)
    response = socket.recv_string()
    print(response)