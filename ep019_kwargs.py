# 调用函数时，可以按照位置传递参数
def remainder(number, divisor):
    return number % divisor

assert remainder(20, 7) == 6

# 所有的位置参数，都可以按照关键字传递
# 还可以混合使用关键字参数和位置参数
remainder(20, 7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)

# 位置参数必须出现在关键字参数之前
# remainder(number=20, 7)
"""
  File "ep019_kwargs.py", line 15
    remainder(number=20, 7)
                        ^
SyntaxError: positional argument follows keyword argument
"""

# 每个参数只能指定一次
# remainder(20, number=7)
"""
Traceback (most recent call last):
  File "ep019_kwargs.py", line 24, in <module>
    remainder(20, number=7)
TypeError: remainder() got multiple values for argument 'number'
"""


# 每秒钟液体的流速
def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff


weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print('%.3f kg per second' % flow)
"""
0.167 kg per second
"""


# 增加时间换算的参数
def flow_rate(weight_diff, time_diff, period):
    return (weight_diff / time_diff) * period

# 即便计算最简单的每秒流率，也要给 period 传入 1
flow_per_second = flow_rate(weight_diff, time_diff, 1)

# 给 period 参数定义默认值
def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period

flow_per_second = flow_rate(weight_diff, time_diff)
flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)


# 根据其它重量单位来计算流率
def flow_rate(weight_diff, time_diff, 
              period=1, units_per_kg=1):
    return ((weight_diff * units_per_kg) / time_diff) * period

# 原代码可以保持不变
# 新代码可以通过指定关键字参数来使用新功能
pounds_per_hour = flow_rate(weight_diff, time_diff,
                            period=3600, 2.2)

# 缺点：仍然可以通过位置参数的形式指定可选的关键字参数。
# 这样容易让人困惑
pounds_per_hour = flow_rate(weight_diff, time_diff, 3600, 2.2)
