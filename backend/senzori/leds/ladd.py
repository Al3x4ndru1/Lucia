from random import randint
import time
from random import seed

import eel


def led():
    while True:
        a=randint(0, 100)
        ON="ON"
        OFF="OFF"
        if a < 60:
            eel.updateLedTurn(ON)

        else:
            eel.updateLedTurn(OFF)

    time.sleep(1)