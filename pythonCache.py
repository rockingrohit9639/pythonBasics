from functools import lru_cache
import time


@lru_cache(maxsize=int(input("Enter maxsize : ")))
def add_two_values(a, b):
    time.sleep(2)
    return a + b

if __name__ == '__main__':
    while True:
        x = int(input("Enter x : "))
        y = int(input("Enter y : "))
        print(add_two_values(x,y))