# 使用列表推导从一个列表生成另一个
names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

# 相同索引处的两个元素有关联的话
# 可以用循环平行迭代列表
# 下面的代码用来找出最长的名字
longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

print(longest_name)
"""
Cecilia
"""

# 使用 enumerate 代替 range 和索引操作相结合的遍历
longest_name = None
max_letters = 0
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

print(longest_name)
"""
Cecilia
"""

# 用 zip 替换通过索引访问多个列表的写法
longest_name = None
max_letters = 0
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

print(longest_name)
"""
Cecilia
"""

# 只要有一个参数耗尽，zip 就停止生成元组
names.append('Rosalind')
for name, count in zip(names, letters):
    print(name)
"""
Cecilia
Lise
Marie
"""
