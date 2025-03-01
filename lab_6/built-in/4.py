import math
import time


def seco(num, ms):
    sec = ms/1000.0

    time.sleep(sec)

    square =  math.sqrt(num)

    return f"Square root of {num} after {ms} milliseconds is {square}"

print(seco(25100, 2123))