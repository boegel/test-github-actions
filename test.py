import time

def test():
    for i in range(30):
        assert(i == i)
        time.sleep(1)
