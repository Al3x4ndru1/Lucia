import time
from random import seed
from random import randint

import eel


def temperature():
    while True:
        eel.updateTemp(randint(0, 100))
        print(randint(-100,100))
        time.sleep(1)
