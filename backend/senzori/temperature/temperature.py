import time
from random import seed
from random import randint
from backend.senzori.leds.ledsw import ladd
import eel


def checktemp(check):
    global checktemp
    checktemp = check
    global times
    times = 5


def luminosity():
    while True:
        global times
        global checktemp
    var = randint(0, 100)
    eel.updateLuminosity(var)
    if var <= checktemp:
        ladd()
        times = 1

    else:
        times = 5
    time.sleep(times)