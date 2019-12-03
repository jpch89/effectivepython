# 挂钩函数
names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))
print(names)
"""
['Plato', 'Socrates', 'Aristotle', 'Archimedes']
"""

from collections import defaultdict

# 自定义 defaultdict 的挂钩函数
def log_missing():
    print('Key added')
    return 0


# 使用挂钩函数
current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
]
# defaultdict([工厂函数[, 可迭代对象]])
result = defaultdict(log_missing, current)
print('Before:', dict(result))
for key, amount in increments:
    result[key] += amount
print('After:', dict(result))
"""
Before: {'green': 12, 'blue': 3}
Key added
Key added
After: {'green': 12, 'blue': 20, 'red': 5, 'orange': 9}
"""


# 使用带状态的闭包
def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count  # Stateful closure
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count


result, count = increment_with_report(current, increments)
assert count == 2


# 自定义辅助类
class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

counter = CountMissing()
result = defaultdict(counter.missing, current)

for key, amount in increments:
    result[key] += amount
assert counter.added == 2


# 定义可调用的对象
class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1

# 测试 BetterCountMissing 的实例是否可调用
counter = BetterCountMissing()
counter()
assert callable(counter)

# 把可调用的对象作为挂钩函数
counter = BetterCountMissing()
result = defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2
