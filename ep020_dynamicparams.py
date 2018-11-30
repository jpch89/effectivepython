from datetime import datetime
from time import sleep

# 动态默认值参数
def log(message, when=datetime.now()):
    print('%s：%s' % (when, message))

log('初次见面，请多关照')
sleep(0.1)
log('这么巧，又见面了')
"""
2018-11-29 10:58:31.444798：初次见面，请多关照
2018-11-29 10:58:31.444798：这么巧，又见面了
"""

# 正确版本的动态默认值参数
def log(message, when=None):
    """Log a message with a timestamp.a

    Args:
        message: Message to print.
        when: datetime of when the message occurred.
            Defaults to the present time.
    """
    when = datetime.now() if when is None else when
    print('%s：%s' % (when, message))

log('初次见面，请多关照')
sleep(0.1)
log('这么巧，又见面了')
"""
2018-11-29 11:09:02.975954：初次见面，请多关照
2018-11-29 11:09:03.076682：这么巧，又见面了
"""

import json
# 读取 JSON 数据，如果失败，返回空字典
def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
"""
Foo: {'stuff': 5, 'meep': 1}
Bar: {'stuff': 5, 'meep': 1}
"""

# 不报错！
assert foo is bar

# 解决方法：使用 None 作为动态参数的默认值
# 在文档字符串中描述动态参数的设置规则
# 在函数定义时判断参数是否为 None
# 如果为 None，进行相应设置
def decode(data, default=None):
    """Load JSON data from a string.

    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default

# 现在就正确了
foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)

"""
Foo: {'stuff': 5}
Bar: {'meep': 1}
"""
