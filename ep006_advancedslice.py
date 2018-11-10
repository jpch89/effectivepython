w = '谢谢你'
x = w.encode('utf-8')
print(x)
y = x[::-1]
# 报错
# UnicodeDecodeError
z = y.decode('utf-8')
