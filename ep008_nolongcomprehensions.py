# 使用两级列表推导展开矩阵
# 推导顺序是从左到右
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)
print('-' * 50)

# 对矩阵每个元素求平方，组成新矩阵
squared = [[x ** 2 for x in row] for row in matrix]
print(squared)
print('-' * 50)

# 假如是三维列表，列表推导要拆成几行才好看
# 不推荐这种写法，因为没有比嵌套循环更清晰方便
my_lists = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
]
flat = [x for sublist1 in my_lists
        for sublist2 in sublist1
        for x in sublist2]
print(flat)
print('-' * 50)

# 此时改成嵌套循环还更清晰些
flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)

# 列表推导支持多个 if 条件
# 多个 if 条件默认以 and 逻辑连接
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x % 2 == 0]  # 推荐！
c = [x for x in a if x > 4 and x % 2 == 0]

# 每一级 for 循环都可以指定 if 条件
# 需求：找出矩阵中可以被 3 整除，并且所在行各元素之和大于 10 的元素
# 列表推导省空间，但是不利于二次阅读！
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]
print(filtered)
