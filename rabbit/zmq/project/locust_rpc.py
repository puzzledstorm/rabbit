import msgpack
import zmq.green as zmq


class Message(object):
    def __init__(self, message_type, data, node_id):
        self.type = message_type
        self.data = data
        self.node_id = node_id

    def serialize(self):
        return msgpack.dumps((self.type, self.data, self.node_id))

    @classmethod
    def unserialize(cls, data):
        msg = cls(*msgpack.loads(data, encoding='utf-8'))
        return msg


class BaseSocket(object):
    def send(self, msg):
        self.sender.send(msg.serialize())

    def recv(self):
        data = self.receiver.recv()
        return Message.unserialize(data)


class Server(BaseSocket):
    def __init__(self, host, port):
        context = zmq.Context()
        self.receiver = context.socket(zmq.PULL)
        self.receiver.bind("tcp://%s:%i" % (host, port))

        self.sender = context.socket(zmq.PUSH)
        self.sender.bind("tcp://%s:%i" % (host, port + 1))


class Client(BaseSocket):
    def __init__(self, host, port):
        context = zmq.Context()
        self.receiver = context.socket(zmq.PULL)
        self.receiver.connect("tcp://%s:%i" % (host, port + 1))

        self.sender = context.socket(zmq.PUSH)
        self.sender.connect("tcp://%s:%i" % (host, port))