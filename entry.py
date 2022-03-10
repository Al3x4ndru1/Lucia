import time
import threading

import eel

import backend.flowers as flower
import backend.python_video_stream.client as camera
import backend.senzori.luminosity.luminosity1 as lum
import backend.senzori.temperature.temperature as temp
import backend.senzori.water.water as water
import backend.senzori.leds.ladd as turn

eel.init('frontend')

flower_thread = threading.Thread(target=flower.flowes)
flower_thread.start()

luminosity_thread = threading.Thread(target=lum.luminosity)
luminosity_thread.start()

# for temperature
Temperature_thread = threading.Thread(target=temp.temperature)
Temperature_thread.start()


#for water
Water_thread = threading.Thread(target=water.water)
Water_thread.start()


#for on/off
Turn_thread = threading.Thread(target=turn.led)
Turn_thread.start()
# for cameras
# camera_thread = threading.Thread(target=camera.client)

eel.start('View.html')
