import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 256)

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