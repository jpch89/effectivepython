# 确保文件能够可靠的关闭文件句柄
handle = open('ep001_version.py')  # May raise IOError
try:
    data = handle.read()  # May raise UnicodeDecodeError
finally:
    handle.close()  # Always run after try:

# 从字符串中加载 JSON 字典数据
def load_json_key(data, key):
    try:
        result_dict = json.loads(data)  # May raise ValueError
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]  # May raise KeyError
