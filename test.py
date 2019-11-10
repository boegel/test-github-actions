import time

def test():
    for i in range(10):
        assert(i == i)
        time.sleep(1)
