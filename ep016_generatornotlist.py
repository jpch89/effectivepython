# 添加词的首字母索引到列表中
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

address = 'Four score and seven years ago...'
result = index_words(address)
print(result[:3])
"""
[0, 5, 11]
"""

# 用生成器函数改写使用列表的代码
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1
# 使用 list 函数可以把生成器转换为列表

# 从文件中一行一行的读取
print('-' * 20)

def index_file(handle):
    offset = 0
    for line in handle:
        # 返回每一行首个单词的首字母的偏移量
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset

with open('my_address.txt') as f:
    it = index_file(f)
    from itertools import islice
    results = islice(it, 0, 3)
    print(list(results))
"""
--------------------
[0, 5, 11]
"""
