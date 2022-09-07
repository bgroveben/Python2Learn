from contextlib import contextmanager
import signal
import time

@contextmanager
def timeout(duration):
    def timeout_handler(signum, frame):
        raise TimeoutError(f'block timedout after {duration} seconds')
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(duration)
    try:
        yield
    finally:
        signal.alarm(0)

def sleeper(duration):
    time.sleep(duration)
    print('finished')

sleeper(10)
