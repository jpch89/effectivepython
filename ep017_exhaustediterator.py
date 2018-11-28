# 返回列表的标准化函数
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
"""
[11.538461538461538, 26.923076923076923, 61.53846153846154]
"""

# 使用生成器从文件读取数据
def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

# 没有返回结果的原因是：
# normalize 中的 sum 函数已经把 生成器 it 耗尽
it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages)
"""
[]
"""

print('-' * 20)
it = read_visits('my_numbers.txt')
print(list(it))
print(list(it))
"""
--------------------
[15, 35, 80]
[]
"""

# 解决方案 1：把输入数据的生成器复制成一份列表
# 缺点：大量输入数据会消耗大量内存
def normalize_copy(numbers):
    numbers = list(numbers)  # 复制生成器
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)
"""
[11.538461538461538, 26.923076923076923, 61.53846153846154]
"""

# 解决方案 2：每次迭代都用一个函数产生新的生成器
# 缺点：使用 lambda 函数显得生硬
def normalize_func(get_iter):
    total = sum(get_iter())  # 新生成器
    result = []
    for value in get_iter():  # 又是一个新生成器
        percent = 100 * value / total
        result.append(percent)
    return result

path = 'my_numbers.txt'
percentages = normalize_func(lambda: read_visits(path))
print(percentages)
"""
[11.538461538461538, 26.923076923076923, 61.53846153846154]
"""

# 解决方案 3：编写实现迭代器协议的类
# 缺点：需要打开两次文件，读取两次输入数据
class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

path = 'my_numbers.txt'
visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)
"""
[11.538461538461538, 26.923076923076923, 61.53846153846154]
"""

# 改进解决方案 3：
# 让 nomralize 函数不接收迭代器作为参数
def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):  # 迭代器 -- 不要！
        raise TypeError('请提供可迭代对象！')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
normalize_defensive(visits)  # 不报错
visits = ReadVisits(path)    # 不报错

# 如果传递迭代器作为参数，会抛出异常
it = iter(ReadVisits(path))
normalize_defensive(it)
"""
Traceback (most recent call last):
  File "ep017_exhaustediterator.py", line 114, in <module>
    normalize_defensive(it)
  File "ep017_exhaustediterator.py", line 100, in normalize_defensive
    raise TypeError('请提供可迭代对象！')
TypeError: 请提供可迭代对象！
"""
