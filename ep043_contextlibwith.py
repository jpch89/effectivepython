from threading import Lock

# Lock 类支持 with 语句
lock = Lock()
with lock:
    print('Lock is held 拿到锁了')

# 等价的 try/finally 写法
lock.acquire()
try:
    print('Lock is held 拿到锁了')
finally:
    lock.release()

