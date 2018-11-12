a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 列表推导
squares = [x ** 2 for x in a]
# map 函数配合匿名函数
squares = map(lambda x: x ** 2, a)

# 列表推导配合 if 条件
even_squares = [x ** 2 for x in a if x % 2 == 0]
# map 配合 filter
alt = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)
