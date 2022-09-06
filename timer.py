import multiprocessing
import time


# bar
def bar():
    for i in range(100):
        print("Tick")
        time.sleep(1)

if __name__ == '__main__':
    # Start bar as a process
    p = multiprocessing.Process(target=bar)
    p.start()

    # Wait for 10 seconds or until process finishes
    p.join(10)

    # If thread is still active
    if p.is_alive():
        print("running... let's kill it...")

        # Terminate - may not work if process is stuck for good
        p.terminate()
        # OR Kill - will work for sure, no chance for process to finish nicely however
        # p.kill()

        p.join()
"""
# Your foo function
def foo(n):
    for i in range(10000 * n):
        print("Tick")
        time.sleep(1)

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo, name="Foo", args=(10,))
    p.start()
    time.sleep(10)
    p.terminate()
    p.join()



def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Time's Up")

countdown(10)
"""
