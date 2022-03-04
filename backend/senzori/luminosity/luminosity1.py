import time
from random import seed
from random import randint
from backend.senzori.leds.ladd import led

import eel


def luminosity():
    while True:
        var = randint(0, 100)
        eel.updateLuminosity(var)
        led(var)
        time.sleep(1)
