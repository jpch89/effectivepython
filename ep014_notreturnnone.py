# 辅助函数，计算两数的商
# 如果出现除零错误，返回 None
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# 判断结果是否为 None
x, y = 4, 0
result = divide(x, y)
if result is None:
    print('Invalid inputs')
"""
Invalid inputs
"""

# 但是我们可能不会专门判断结果是否为 None
# 而是假定如果 result 为 False，那么说明函数出错了
x, y = 0, 4
result = divide(x, y)
if not result:
    print('Invalid inputs')  # This is wrong!
"""
Invalid inputs
"""

# 解决方案1：
# 返回一个二元组 two-tuple
# 二元组的第一个元素表示操作是否成功
# 第二个元素表示结果
def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None

x, y = 4, 0
success, result = divide(x, y)
if not success:
    print('Invalid inputs')
"""
Invalid inputs
"""

# 但是调用者可以用下划线 _ 忽略不想要的第一部分
# 这样还是会出错
x, y = 0, 4
_, result = divide(x, y)
if not result:
    print('Invalid inputs')
"""
Invalid inputs
"""

# 解决方案2（最好的方案）：
# 向上一级抛出异常
# 把 ZeroDivisionError 转化成 ValueError
# 表示调用者给的输入值无效
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e

x, y = 4, 0
result = divide(x, y)
print(result)
"""
Traceback (most recent call last):
  File "ep014_notreturnnone.py", line 62, in divide
    return a / b
ZeroDivisionError: division by zero

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "ep014_notreturnnone.py", line 67, in <module>
    result = divide(x, y)
  File "ep014_notreturnnone.py", line 64, in divide
    raise ValueError('Invalid inputs') from e
ValueError: Invalid inputs
"""

# 现在调用者必须处理因输入值无效而引发的异常
# 不用判断返回结果，因为如果没有异常，结果就是正确的
x, y = 5, 2
try:
    result = divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)
"""
Result is 2.5
"""
