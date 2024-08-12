import select
import sys
import os

f = open("log.txt", "w")
os.dupterm(f)

from controllers.builtin_led_controller import builtin_led_controller
from controllers.led_strip_controller import led_strip_controller

try:

    poll_obj = select.poll()
    poll_obj.register(sys.stdin, select.POLLIN)

    
    while True:

        poll_results = poll_obj.poll(1)
        if poll_results:

            data = list(sys.stdin.readline().strip().split())
            status = ""
            
            if not data:
                continue

            if data[0] == "25":
                status = builtin_led_controller(data[1:])
                
            elif data[0] == "16":
                status = led_strip_controller(data[1:])
            
            sys.stdout.write(status)

        else:
            continue
except KeyboardInterrupt:
    f.close()
    raise KeyboardInterrupt
except Exception as e:
    raise(e)
