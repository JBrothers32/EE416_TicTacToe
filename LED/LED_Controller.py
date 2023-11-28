import board
import neopixel
import time
from rpi_ws281x import Adafruit_NeoPixel, Color

# pixels = neopixel.NeoPixel(board.D18, 256)

pixel_pin = board.D18
num_pixels = 256
freq = 800000
dma = 10
brightness = 180
invert = False
ORDER = neopixel.RGB

# pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, 
#                            auto_write=False, pixel_order=ORDER)


#[start_row_num,start_col_num]
led_zones = {
    "00":[2,2],
    "01":[2,7],
    "02":[2,12],
    "10":[7,2],
    "11":[7,7],
    "12":[7,12],
    "20":[12,2],
    "21":[12,7],
    "22":[12,12]
}

def LightZone(zone, color):
    zone_row = led_zones[zone][0]
    zone_col = led_zones[zone][1]
    for row in range(4):
        for col in range (4):
            pixels[((zone_row + row) - 1 * 16 )+(zone_col + col)] = color

# LightZone("00", (51,204,51))
# pixels.show()
# time.sleep(10)
# del(pixels)
if __name__ == '__main__':
    # pixels[15] = (51,204,51)
    # pixels.show()
    pixels = Adafruit_NeoPixel(num_pixels, pixel_pin, freq, dma, invert, brightness)
    pixels.begin()
    pixels.setPixelColor(15, Color(51,204,51))
    pixels.show()
    time.sleep(2)