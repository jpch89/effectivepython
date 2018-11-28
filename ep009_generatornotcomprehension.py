value = [len(x) for x in open('ep001_version.py')]
print(value)
"""
[11, 24, 19, 1, 4, 76, 77, 4]
"""

it = (len(x) for x in open('ep001_version.py'))
print(it)
print(next(it))
print(next(it))
"""
<generator object <genexpr> at 0x0000023D58EAAA40>
11
24
"""

roots = ((x, x ** 0.5) for x in it)
print(next(roots))
"""
(19, 4.358898943540674)
"""
