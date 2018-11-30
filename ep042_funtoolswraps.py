def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
              (func.__name__, args, kwargs, result))
        return result

    return wrapper


@trace  # 等价于：fibonacci = trace(fibonacci)
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


fibonacci(3)
"""
fibonacci((1,), {}) -> 1
fibonacci((0,), {}) -> 0
fibonacci((1,), {}) -> 1
fibonacci((2,), {}) -> 1
fibonacci((3,), {}) -> 2
"""

# 副作用：装饰器返回的那个值，名称和原函数不同
print(fibonacci)
"""
<function trace.<locals>.wrapper at 0x0000022B20B9A6A8>
"""

# fibonacci 的 help 失效
print(help(fibonacci))
"""
Help on function wrapper in module __main__:

wrapper(*args, **kwargs)

None
"""

from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
              (func.__name__, args, kwargs, result))
        return result

    return wrapper


@trace  # 等价于：fibonacci = trace(fibonacci)
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


print(help(fibonacci))
"""
Help on function fibonacci in module __main__:

fibonacci(n)
    Return the n-th Fibonacci number

None
"""
