from functools import lru_cache
import time

@lru_cache(maxsize=None)
def slow_function(n):
    time.sleep(2)   # simulate delay
    return n * n

print(slow_function(5))  # Takes 2 sec
print(slow_function(6))  # Takes 2 sec
print(slow_function(5))  # Instant 
print(slow_function(6))  # Instant