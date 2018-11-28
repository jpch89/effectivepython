# 正常循环完毕执行 else 块
for i in range(3):
    print('循环 %d' % i)
else:
    print('else 块！')
"""
循环 0
循环 1
循环 2
else 块！
"""

# 中断循环则不会执行 else 块
for i in range(3):
    print('循环 %d' % i)
    if i == 1:
        break
else:
    print('else 块！')
"""
循环 0
循环 1
"""

# 如果被遍历的对象是空的，会立即执行 else 块
for x in []:
    print('永远不会执行！')
else:
    print('我是 else 块！')
"""
我是 else 块！
"""

# 循环初始条件为 False，也会立即执行 else 块
while False:
    print('永远不会执行！')
else:
    print('我是 else 块！')
"""
我是 else 块！
"""

# 判断两个数是否互质 coprime
# 即除了 1 以外，没有其他公约数
a = 4
b = 9
for i in range(2, min(a, b) + 1):
    print('尝试', i)
    if a % i == 0 and b % i == 0:
        print('不互质！')
        break
else:
    print('互质！')
"""
互质！
"""

# 使用辅助函数判断是否互质（写法1）
def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

# 使用辅助函数判断是否互质（写法2）
def coprime2(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime
