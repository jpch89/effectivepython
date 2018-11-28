# range 在一系列整数上迭代很有用
# 比如下面的代码可以生成 64 位二进制随机数
from random import randint

random_bits = 0
for i in range(64):
    if randint(0, 1):
        random_bits |= 1 << i

print(bin(random_bits))
"""
0b11100111001101100000001111011001111100010001101010111101101101
"""

# 迭代一个列表
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print('%s is delicious' % flavor)
"""
vanilla is delicious
chocolate is delicious
pecan is delicious
strawberry is delicious
"""

# 迭代的同时获取索引
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d: %s' % (i + 1, flavor))
"""
1: vanilla
2: chocolate
3: pecan
4: strawberry
"""

# 使用 enumerate 代替 range 与下标相结合的遍历代码
for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i + 1, flavor))
"""
1: vanilla
2: chocolate
3: pecan
4: strawberry
"""

# enumerate 第二个参数指定初始值
for i, flavor in enumerate(flavor_list, 1):
    print('%d: %s' % (i, flavor))
"""
1: vanilla
2: chocolate
3: pecan
4: strawberry
"""
