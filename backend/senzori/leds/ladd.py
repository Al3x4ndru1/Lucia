import eel


def led(luminosity):
    if luminosity < 60:
        eel.updateLed("Off")
    else:
        eel.updateLed("On")