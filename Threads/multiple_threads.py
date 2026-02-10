import time
import threading


def calc_square():
    for i in range(1000):
        a = i**2
        time.sleep(0.001)
    return

def calc_root():
    for i in range(1000):
        a = i**0.5
        time.sleep(0.001)
    return

task_1 = threading.Thread(target=calc_square)
task_2 = threading.Thread(target=calc_root)

start_time  = time.time()  # Multiple thread

task_1.start() # Task_1 start
task_2.start() # Task_2 start (Not until task_1 end)
task_1.join()
task_2.join()

end_time = time.time() # Get time when 2 threads are all end
print("multiple thread end")
print(f"It cost {end_time - start_time} seconds.") # 1.5446999073028564


start_time_second = time.time() # Single thread

calc_root() 
calc_square()

end_time_second = time.time()
print("Single thread end")
print(f"It cost {end_time_second - start_time_second} seconds.") # 3.2256951332092285

'''
Multiple threads run faster than single thread 

'''



