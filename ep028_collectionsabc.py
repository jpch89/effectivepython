class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1
        return counts

# 继承于 list 的类拥有 list 提供的全部标准功能
foo = FrequencyList(['a', 'b', 'a', 'c', 'b', 'a', 'd'])
print('长度为：%s' % len(foo))
foo.pop()
print('弹出之后为：%s' % repr(foo))
print('频率为：%s' % foo.frequency())
"""
长度为：7
弹出之后为：['a', 'b', 'a', 'c', 'b', 'a']
频率为：{'a': 3, 'b': 2, 'c': 1}
"""

