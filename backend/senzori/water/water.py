import time
from random import seed
from random import randint

import eel


def water():
    while True:
        eel.updateWater(randint(0, 100))
        time.sleep(1)
