import time
from random import seed
from random import randint
from backend.senzori.leds.ledsw import ladd

import eel

global check
global times
times=5

def importcheck(check):
    check=check



def luminosity():
    while True:
        var = randint(0, 100)
        eel.updateLuminosity(var)
        if var<=check:
            ladd()
            times=1
        else:
            times=5

        time.sleep(times)
