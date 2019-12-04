import os
from tempfile import TemporaryDirectory
from threading import Thread


class InputData(object):
    def read(self):
        raise NotImplementedError


class PathInputData(InputData):
    """来自磁盘文件的输入数据类"""

    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()


class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


class LineCountWorker(Worker):
    def map(self):
        # 调用了输入数据类实例的 read 方法
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads:
        thread.start()
    # join 的作用是线程同步，可以让主线程等待所有子线程的完成再终止
    for thread in threads:
        thread.join()

    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result


def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)


def write_test_files(tempdir):
    # 团子注：这个是我自己随便写的内容
    with open(os.path.join(tempdir, 'tmp1.txt'), 'w') as f:
        f.write('四\n个\n换\n行\n')
    with open(os.path.join(tempdir, 'tmp2.txt'), 'w') as f:
        f.write("""为了看看阳光
        我来到这世上
        莱蒙托夫
        """)


with TemporaryDirectory() as tmpdir:
    write_test_files(tmpdir)
    result = mapreduce(tmpdir)

print('There are', result, 'lines')
"""
There are 7 lines
"""

# 下面的代码仅用作说明，并没有通过测试，所以注释掉了
"""
class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    # 团子注：这里省略了 __init__

    def read(self):
        return open(self.path).read()
    
    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker(object):
    # ...

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers
    

class LineCountWorker(GenericWorker):
    # 团子注：这里需要定义 map 和 reduce 方法
    pass


def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)


with TemporaryDirectory() as tmpdir:
    write_test_files(tmpdir)
    config = {'data_dir': tmpdir}
    result = mapreduce(LineCountWorker, PathInputData, config)
"""
