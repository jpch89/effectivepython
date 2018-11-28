# 把 numbers 中出现在 group 里面的数字放在前面
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)
"""
[2, 3, 5, 7, 1, 4, 6, 8]
"""

# 新需求：判断 numbers 的数字是否出现在了 group 里面
def sort_priority2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True  # 看起来很简单
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
found = sort_priority2(numbers, group)
print('Found:', found)
print(numbers)
# 明明找到了，但是却显示没有找到！
"""
Found: False
[2, 3, 5, 7, 1, 4, 6, 8]
"""

def sort_priority2(numbers, group):
    found = False         # Scope: 'sort_priority2'
    def helper(x):
        if x in group:
            found = True  # Scope: 'helper' -- Bad!
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

def sort_priority3(numbers, group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
found = sort_priority3(numbers, group)
print('Found:', found)
print(numbers)
"""
Found: True
[2, 3, 5, 7, 1, 4, 6, 8]
"""

print('-' * 30)
class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)

sorter = Sorter(group)
numbers.sort(key=sorter)
print(numbers)
assert sorter.found is True

"""
------------------------------
[2, 3, 5, 7, 1, 4, 6, 8]
"""

# Python 2
def sort_priority(numbers, group):
    found = [False]
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found[0]
