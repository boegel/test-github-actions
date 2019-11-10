import time

def test():
    for i in range(15):
        assert(i == i)
        time.sleep(1)
