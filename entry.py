import time
import threading

import eel

import backend.flowers as flower
import backend.python_video_stream.client as camera
import backend.senzori as senzori
import backend.senzori.temperature.temperature as temp

eel.init('frontend')

flower_thread = threading.Thread(target=flower.flowes)
flower_thread.start()

# luminosity_thread =threading.Thread(target=senzori.luminosity)
# luminosity_thread.start()

# for temperature
Temperature_thread = threading.Thread(target=temp.temperature)
Temperature_thread.start()

# for cameras
# camera_thread = threading.Thread(target=camera.client)

eel.start('View.html')
