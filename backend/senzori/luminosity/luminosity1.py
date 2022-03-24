import time
from random import seed
from random import randint
from backend.senzori.leds.ledsw import ladd

import eel


def luminosity(check):
    while True:
        var = randint(0, 100)
        eel.updateLuminosity(var)
        if var <check:
            ladd()
        time.sleep(5)
