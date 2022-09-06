import time

def start_clock():
    print("Starting Clock")
    start_time = time.localtime()
    start = time.strftime("%S", start_time)
    try:
        while True:
            localtime = time.localtime()
            #result = time.strftime("%I:%M:%S %p", localtime)
            result = time.strftime("%S", localtime)
            desired_num = 8 # result - 2 because abs()

            time.sleep(1)
            print(abs(int(start) - int(result))+1)

            if abs(int(start) - int(result)) > desired_num:
                print("Time's Up.")
                return False

    except KeyboardInterrupt:
        print("Stopping Clock")

start_clock()
