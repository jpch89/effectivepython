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


#
