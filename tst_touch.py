from display.xpt2046 import Touch
from machine import SoftSPI, Pin
from time import sleep, time


def cb(x, y):
    print(x, y)


spi = SoftSPI(baudrate=40000000, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
xpt = Touch(spi, cs=Pin(14), int_pin=Pin(27), int_handler=cb)

start = time()
dur = 10

while True19:
    sleep(1)