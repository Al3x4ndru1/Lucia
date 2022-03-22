import time
from random import seed
from random import randint

import eel

def intoduce(plants, type):
    global nuplants
    nuplants=plants
    global planttype
    planttype=type
    global capacity
    capacity=100


def water():
    while True:
        #waterL=capacity-(nuplants*planttype)

        global  capacity
        print(capacity)
        capacity = capacity - ((nuplants * planttype)/10)
        if capacity<=40:
            capacity=100
            print("Refulling, takeing a break for 10 seconds")
            time.sleep(10)

        eel.updateWater(capacity)
        time.sleep(5)
