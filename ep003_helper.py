from urllib.parse import parse_qs

# 解析查询字符串 query string
my_values = parse_qs('red=5&blue=0&green=',
                     keep_blank_values=True)
# print(repr(my_values))  # 原书写法
print(my_values)  # 返回的是字典，直接这样写就行了
# >>>
# {'red': ['5'], 'blue': ['0'], 'green': ['']}

# 查询字符串中的参数可能有：多个值和空白 blank 值。
# 有些参数则没有出现。
# 使用 get 方法可以不报错的从字典中取值。
print('Red:     ', my_values.get('red'))
print('Green:   ', my_values.get('green'))
print('Opacity: ', my_values.get('opacity'))

print('-' * 50)
# 需求：当查询的参数没有出现在查询字符串中
# 或者参数的值为空白的时候
# 可以返回 0
# 思路：空值和零值都是 False
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print('Red:     %r' % red)
print('Green:   %r' % green)
print('Opacity: %r' % opacity)

print('-' * 50)
# 需求：最后要用到的是整数类型
# 思路：类型转换
red = int(my_values.get('red', [''])[0] or 0)
# 这种长表达式的写法看上去很乱！

# 改进1：使用 Python 2.5 添加的三元表达式
red = my_values.get('red', [''])
red = int(red[0]) if red[0] else 0

# 改进2：使用跨行的 if/else 语句
green = my_values.get('green', [''])
if green[0]:
    green = int(green[0])
else:
    green = 0


# 改进3：频繁使用的逻辑，需要封装成辅助函数
def get_first_value(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found
