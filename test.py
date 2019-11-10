import time

def test():
    for i in range(25):
        assert(i == i)
        time.sleep(1)
