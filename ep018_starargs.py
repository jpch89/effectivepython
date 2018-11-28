def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s：%s' % (message, values_str))

log('My numbers are', [1, 2])
log('Hi there', [])
"""
My numbers are：1, 2
Hi there
"""

def log(message, *values):  # 只改动了这里
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s：%s' % (message, values_str))

log('My numbers are', 1, 2)
log('Hi there')  # 这样写好多了
"""
My numbers are：1, 2
Hi there
"""

favorites = [7, 33, 99]
log('Favorite colors', *favorites)
"""
Favorite colors：7, 33, 99
"""

# 变长参数问题 1：
# 传入生成器会存储为元组
# 数据量较大消耗内存也会变大
def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)
"""
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
"""

# 变长参数问题 2：
# 添加位置参数需要修改函数定义和函数调用
# 忘记修改调用会发生难以调试的错误
def log(sequence, message, *values):
    if not values:
        print('%s: %s' % (sequence, message))
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s: %s' % (sequence, message, values_str))


log(1, 'Favorites', 7, 33)        # 新用法没问题
log('Favorite numbers', 7, 33)    # 旧用法会出错
"""
1: Favorites: 7, 33
Favorite numbers: 7: 33
"""
