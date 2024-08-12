from machine import Pin

def builtin_led_controller(data):
    
    led = Pin(25, Pin.OUT)
    
    if data[0] == "1":
        led.value(1)
        return "LED turned on\n"
        
                        
    elif data[0] == "0":
        led.value(0)
        return "LED turned off\n"
