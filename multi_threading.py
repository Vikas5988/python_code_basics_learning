import threading
import time

# perf_counter gives the most precise time measurement
# more accurate than time.time() for short durations
start = time.perf_counter()

# task function — simulates a job that takes time
def fetch(name, delay):
    print(f"{name} started...")
    time.sleep(delay)          # simulates work (network call, file read)
    print(f"{name} done!")

# create threads — each thread runs fetch() independently
t1 = threading.Thread(target=fetch, args=("Task 1", 3))
t2 = threading.Thread(target=fetch, args=("Task 2", 1))
t3 = threading.Thread(target=fetch, args=("Task 3", 2))

# start all threads — they run CONCURRENTLY
t1.start()
t2.start()
t3.start()

# join() — main program WAITS for all threads to finish
t1.join()
t2.join()
t3.join()

end = time.perf_counter()

# round() limits decimal places for clean output
print(f"Total Time: {round(end - start, 1)} sec")