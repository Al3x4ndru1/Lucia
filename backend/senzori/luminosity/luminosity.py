import math
import sys
import time
import grove.adc
import ADC


class GroveLightSenzor:
    def __init__(self,channel):
        self.channel = channel
       # self.adc = ADC()


    @property
    def light(self):
        value = self.adc.read(self.channel)
        return value



Grove = GroveLightSenzor


def main() -> int :
    if len(sys.argv) < 2:
        print('Usge: '.format(sys.argv[0]))
        sys.exit(1)


    sensor = GroveLightSenzor(int(sys.argv[1]))

    print('Detecting light...')

    while True:
        print('Light senzor value: [0]'.format(sensor.light))
        time.sleep(1)

if __name__ == '__main__':
    main()