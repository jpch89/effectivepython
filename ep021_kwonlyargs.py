def safe_division(number, divisor,
    ignore_overflow, ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

# 忽略 float 溢出错误，并返回 0
result = safe_division(1.0, 10 ** 500, True, False)
print(result)
"""
0
"""

# 忽略除零错误，并返回无穷
result = safe_division(1, 0, False, True)
print(result)
"""
inf
"""

# 改进：把后面两个参数定义为关键字参数
def safe_division_b(number, divisor,
                ignore_overflow=False,
                ignore_zero_division=True):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

# 调用者按需覆盖默认参数
safe_division_b(1, 10 ** 500, ignore_overflow=True)
safe_division_b(1, 0, ignore_zero_division=True)

# 缺点：仍然可以用位置参数的形式来调用
safe_division_b(1, 10 ** 500, True, False)

# 改进：使用强制关键字参数
def safe_division_c(number, divisor, *,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

# 再使用位置参数指定就会出错
# safe_division_c(1, 10 ** 500, True, False)
"""
Traceback (most recent call last):
  File "ep021_kwonlyargs.py", line 72, in <module>
    safe_division_c(1, 10 ** 500, True, False)
TypeError: safe_division_c() takes 2 positional arguments but 4 were given
"""

# 如果不指定关键字参数，默认值会生效
safe_division_c(1, 0, ignore_zero_division=True)
# 不报错！

try:
    safe_division_c(1, 0)
except ZeroDivisionError:
    print('捕捉到了除零异常！')
"""
捕捉到了除零异常！
"""

# Python 2
def print_args(*args, **kwargs):
    print 'Positional:', args
    print 'Keyword:', kwargs

print_args(1, 2, foo='bar', stuff='meep')
"""
Positional: (1, 2)
Keyword: {'foo': 'bar', 'stuff': 'meep'}
"""

# 模拟强制关键字参数
# Python2
def safe_division_d(number, divisor, **kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow', False)
    ignore_zero_division = kwargs.pop('ignore_zero_division', False)
    if kwargs:
        raise TypeError('Unexpected **kwargs: %r' % kwargs)

# 现在可以正常使用
safe_division_d(1, 10)
safe_division_d(1, 0, ignore_zero_division=True)
safe_division_d(1, 10 ** 500, ignore_overflow=True)

# 不可以通过位置参数指定关键字参数的值
safe_division_d(1, 0, False, True)  # 会报错

# 也不可以传入不符合预期的关键字参数
safe_division_d(0, 0, unexpected=True)
