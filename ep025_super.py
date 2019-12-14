class MyBaseClass(object):
    def __init__(self, value):
        self.value = value
    

class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)


class TimesTwo(object):
    def __init__(self):
        self.value *= 2


class PlusFive(object):
    def __init__(self):
        self.value += 5


class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


foo = OneWay(5)
print('First ordering is (5 * 2) + 5 =', foo.value)
"""
First ordering is (5 * 2) + 5 = 15
"""


class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


bar = AnotherWay(5)
print('Second ordering still is', bar.value)
"""
Second ordering still is 15
"""


class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5


class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2


class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)


foo = ThisWay(5)
print('Should be (5 * 5) + 2 = 27 but is', foo.value)
"""
Should be (5 * 5) + 2 = 27 but is 7
"""


# Python 2
class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(TimesFiveCorrect, self).__init__(value)
        self.value *= 5


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value += 2


class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)


foo = GoodWay(5)
# 团子注：原书为下面一句，但是为了在 Python 3 中运行，我加了括号，结果是一样的！
# print 'Should be 5 * (5 + 2) = 35 and is ', foo.value
print('Should be 5 * (5 + 2) = 35 and is', foo.value)
"""
Should be 5 * (5 + 2) = 35 and is 35
"""

from pprint import pprint

pprint(GoodWay.mro())
"""
[<class '__main__.GoodWay'>,
 <class '__main__.TimesFiveCorrect'>,
 <class '__main__.PlusTwoCorrect'>,
 <class '__main__.MyBaseClass'>,
 <class 'object'>]
"""


# python 3
class Explicit(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value * 2)


class Implicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value * 2)
