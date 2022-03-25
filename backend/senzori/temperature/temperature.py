import time
from random import seed
from random import randint

import eel

global check
global times
times=5

def importcheck(check):
    check=check

def temperature():
    while True:
        var=randint(0,100)
        eel.updateTemp(var)
        if var <= check:
            print("Alert is too much heat!!!")
            times=1
        else:
            times=5
        time.sleep(times)
