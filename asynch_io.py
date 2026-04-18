import asyncio
import time

# ============================================================
#  SYNCHRONOUS VERSION
# ============================================================

# regular function — no 'async' keyword
def fetch_sync(name, delay):
    print(f"{name} started...")
    
    # time.sleep() FREEZES the entire program
    # nothing else can run until this finishes
    time.sleep(delay)
    
    print(f"{name} done!")

def run_sync():
    print("=" * 40)
    print("SYNCHRONOUS (one by one)")
    print("=" * 40)
    
    # time.time() records the current time
    # used to calculate total execution time
    start = time.time()

    # each task WAITS for the previous one to fully finish
    # Task 2 won't start until Task 1 is completely done
    fetch_sync("Task 1", 3)    # 3 sec — program freezes here
    fetch_sync("Task 2", 1)    # 1 sec — program freezes here
    fetch_sync("Task 3", 2)    # 2 sec — program freezes here

    end = time.time()
    
    # end - start gives total seconds elapsed
    print(f"Total Time: {end - start:.1f} sec\n")  # 3+1+2 = 6 sec


# ============================================================
#  ASYNCHRONOUS VERSION
# ============================================================

# 'async def' marks this as a coroutine
# meaning it CAN be paused and resumed later
async def fetch_async(name, delay):
    print(f"{name} started...")
    
    # 'await' pauses ONLY this task
    # while waiting, other tasks are FREE to run
    # this is the key difference from time.sleep()
    await asyncio.sleep(delay)
    
    print(f"{name} done!")

# 'async def' because it uses 'await' inside
async def run_async():
    print("=" * 40)
    print("ASYNCHRONOUS (all at once)")
    print("=" * 40)
    
    start = time.time()

    # asyncio.gather() runs ALL tasks CONCURRENTLY
    # it starts all 3 tasks and manages them together
    # tasks pause and resume while others are waiting
    await asyncio.gather(
        fetch_async("Task 1", 3),  # starts immediately
        fetch_async("Task 2", 1),  # starts immediately
        fetch_async("Task 3", 2),  # starts immediately
    )

    end = time.time()
    
    # total time = longest task (3 sec), not sum (6 sec)
    print(f"Total Time: {end - start:.1f} sec\n")


# ============================================================
#  RUN BOTH
# ============================================================

# run sync first — notice how it blocks step by step
run_sync()

# asyncio.run() starts the EVENT LOOP
# the event loop is the engine that manages all async tasks
# it decides which task to run, pause, or resume
asyncio.run(run_async())