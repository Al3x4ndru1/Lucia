import time
from random import seed
from random import randint
from backend.senzori.leds.ledsw import ladd
import eel
def checklum(check):
 global checklum
 checklum=check
 global times
 times=5
def luminosity():
    while True:
     global times
    global checklum
    var = randint(0, 100)
    eel.updateLuminosity(var)
    if var<=checklum:
        ladd()
        times = 1

    else:
         times=5
    time.sleep(times)