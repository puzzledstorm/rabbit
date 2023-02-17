# https://blog.csdn.net/Runner1st/article/details/96481954

def test1():
    import logging
    logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        level=logging.DEBUG)

    logger = logging
    logger.info("123")


def test2():
    import logging
    logger = logging.getLogger('test')
    logger.setLevel(level=logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    file_handler = logging.FileHandler('test2.log')
    file_handler.setLevel(level=logging.INFO)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    logger.debug('debug级别，一般用来打印一些调试信息，级别最低')
    logger.info('info级别，一般用来打印一些正常的操作信息')
    logger.warning('waring级别，一般用来打印警告信息')
    logger.error('error级别，一般用来打印一些错误信息')
    logger.critical('critical级别，一般用来打印一些致命的错误信息，等级最高')


if __name__ == '__main__':
    test1()
    test2()
