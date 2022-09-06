from multiprocessing import Process
import time

class TimeoutException(Exception):
    pass

timer = 5
def start_timer():
    time.sleep(timer)
    raise TimeoutException

def lazy_func():
    time.sleep(10)


def scrolldown():
    try:
        lazy_func()
    except TimeoutException:
        print("timeout")
        i += 1

p1 = Process(target=start_timer)
p2 = Process(target=scrolldown)

i = 0
while True:
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    if i == 2:
        break
