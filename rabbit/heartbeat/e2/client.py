## https://blog.csdn.net/zhouchen1998/article/details/122492922

import os
import socket
import time
import threading
import json
import logging

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)
logger = logging


class TCPSocket(object):
    def __init__(self, size, ip, port):
        """
        @param size: 报文上限大小
        @param ip: ip地址
        @param port: 端口
        """
        self.sk = None
        self.size = size
        self.format = "utf8"
        self.ip_port = (ip, port)
        self.logger = logger

        self.msg_type = ['LOGIN', 'HEART']
        self.login_dict = {
            "code": "LOGIN",
        }
        # 心跳频率
        self.heart_interval = 5
        self.status_interval = 5
        self.adapt_time = False

    # 建立socket连接
    def connect(self):
        self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sk.connect(self.ip_port)
        except Exception as e:
            self.logger.error(f"connect to server failed，prepare to reconnect: {e}")
            self.reconnect()

    # 重新连接 5s/次
    def reconnect(self):
        self.logger.info("try to reconnect")
        while True:
            try:
                self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sk.connect(self.ip_port)
                self.login_send()
                self.logger.info(f"client start connect to host/port:{self.ip_port}")
                break
            except ConnectionRefusedError:
                self.logger.error(
                    'socket server refused or not started, reconnect to server in 5s .... host/port:{}'.format(
                        self.ip_port))
                time.sleep(5)

            except Exception as e:
                self.logger.error(f'do connect error:{e}')
                time.sleep(5)
        self.logger.info("reconnect successfully!!!")

    # 发送登录验证
    def login_send(self):
        try:
            login_msg = self.build_request_json("LOGIN", **self.login_dict)
            self.sk.send(login_msg.encode(self.format))
            self.logger.info("[tcp client] send logon message:{}".format(login_msg.replace(os.linesep, "")))
        except socket.error:
            self.logger.info('socket error,do reconnect')
            time.sleep(5)
        except Exception as e:
            self.logger.error(e)
            time.sleep(5)

    def rec(self):
        while True:
            try:
                message = self.sk.recv(self.size)
                messages = self.parse_response_json(message)
                if messages:
                    for msg in messages:
                        if msg['code'] == "LOGIN":
                            # 登录成功
                            self.logger.info("[tcp client] receive logon response: {}".format(msg))
                        elif msg['code'] == "HEART":
                            # 收到心跳反馈
                            self.logger.info("[tcp client] receive heart response: {}".format(msg))
                        else:
                            self.logger.warning("message queue is not supported!!!")
                else:
                    self.logger.info("no message from server or messages are not valid:{}".format(messages))
            except socket.error as e:
                self.logger.error(e)
                time.sleep(5)
                self.reconnect()
            except Exception as e:
                self.logger.error(e)
                time.sleep(5)

    # 间隔固定时间发送心跳
    def heartbeats(self):
        while True:
            try:
                msg = self.build_request_json("HEART")
                self.sk.send(msg.encode(self.format))
                self.logger.info("[tcp client] send heart message:{}".format(msg.replace(os.linesep, "")))
            except socket.error:
                self.logger.error('socket error,do reconnect')
                self.reconnect()
            except Exception as e:
                self.logger.error(f'other error occur: {e}')
                time.sleep(5)
                self.reconnect()
            time.sleep(self.heart_interval)

    @staticmethod
    def build_request_json(method: str, **args) -> str:
        """
        :param method: 该请求的方法类型
        :return: 构建好的用于和服务端通信的Json数据
        """
        if method == "LOGIN":
            json_data = {
                "code": "LOGIN",
            }
        elif method == "HEART":
            json_data = {
                "code": "HEART",
            }
        else:
            print("this method {} is not supported now!!!".format(method))
            json_data = None

        return json.dumps(json_data) + os.linesep if json_data else None

    def parse_response_json(self, data: bytes):
        msgs = []
        try:
            data_list = data.decode(self.format).split(os.linesep)
            data_list = list(filter(lambda x: x.strip().startswith("{"), data_list))

            for msg in data_list:
                msg = json.loads(msg)
                if msg['code'] in self.msg_type:
                    msgs.append(msg)
            return msgs
        except Exception as e:
            self.logger.error(e)
        return None


if __name__ == '__main__':
    socket1 = TCPSocket(1024, "127.0.0.1", 5433)
    socket1.connect()
    socket1.login_send()
    t1 = threading.Thread(target=socket1.rec)
    t2 = threading.Thread(target=socket1.heartbeats)

    t1.start()
    t2.start()
