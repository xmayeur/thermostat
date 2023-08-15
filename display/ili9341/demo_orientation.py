"""ILI9341 demo (orientation)."""
from time import sleep

from display.xglcd_font import XglcdFont
from machine import Pin, SPI

from display.ili9341 import Display, color565


def test():
    """Test code."""
    print('Loading Espresso Dolce font...')
    espresso_dolce = XglcdFont('lib/display/fonts/EspressoDolce18x24.c', 18, 24)
    print('Font loaded.')
    # Baud rate of 40000000 seems about the max
    spi = SPI(2, baudrate=40000000, sck=Pin(18), mosi=Pin(23))

    display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(22), width=240, height=320, rotation=0)
    display.draw_text(0, 0, 'Espresso Dolce 18x24', espresso_dolce, color565(0, 255, 255))
    display.draw_text(0, 319, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(255, 255, 0), landscape=True)
    sleep(5)

    display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(22), width=320, height=240, rotation=90)
    display.draw_text(0, 215, 'Espresso Dolce 18x24', espresso_dolce, color565(255, 0, 255))
    display.draw_text(295, 239, 'Espresso Dolce 18x24', espresso_dolce, color565(255, 255, 255), landscape=True)
    sleep(5)

    display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(22), width=240, height=320, rotation=180)
    display.draw_text(0, 0, 'Espresso Dolce 18x24', espresso_dolce, color565(0, 0, 255))
    display.draw_text(0, 319, 'Espresso Dolce 18x24', espresso_dolce, color565(255, 0, 0), landscape=True)
    sleep(5)

    display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(22), width=320, height=240, rotation=270)
    display.draw_text(0, 215, 'Espresso Dolce 18x24', espresso_dolce, color565(225, 0, 128))
    display.draw_text(295, 239, 'Espresso Dolce 18x24', espresso_dolce, color565(0, 255, 0), landscape=True)
    sleep(5)
    display.cleanup()


test()
