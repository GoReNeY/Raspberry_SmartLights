import time
from libs.neopixel import Neopixel

def led_strip_controller(data):

    numpix = 8
    strip = Neopixel(numpix, 0, 16, "GRB")
    color = ()
    brightness = 1

    new_brightness = int(data[0])
    new_color = tuple(int(i) for i in data[1:])
    
    if new_brightness != brightness:
        brightness = new_brightness
        strip.brightness(brightness)
    
    if new_color != color:
        
        color = new_color
        for i in range(numpix):
            pass
            strip.set_pixel(i, color)
            strip.show()
            
    return "OK\n"
