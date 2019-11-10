import time

def test():
    for i in range(20):
        assert(i == i)
        time.sleep(1)
