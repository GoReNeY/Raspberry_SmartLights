from serial import Serial

def built_in_led_controller(value: str):
    ser=Serial('COM3')

    built_in_led_code = "25"

    if value == "Turn on LED":
        output = ("1")
        ser.write( (" ".join((built_in_led_code, *output)) + "\r\n").encode() )

    elif value == "Turn off LED":
        output = ("0")
        ser.write( (" ".join((built_in_led_code, *output)) + "\r\n").encode() )

    else:
        print("ERROR")
        ser.close()
        return

    mes = ser.read_until(b"\n").strip()

    print(mes.decode())
    ser.close()


def strip_color_controller(value: dict):
    ser=Serial('COM3')

    led_strip_code = "16"

    color = value["color"].lstrip("#")

    if len(color) != 6:
        print("Invalid hex value")
        return

    output = (value["brightness"], ) + tuple(str(int(color[i:i+2], 16)) for i in (0, 2, 4))

    ser.write( (" ".join((led_strip_code, *output)) + "\r\n").encode() )

    mes = ser.read_until(b"\n").strip()

    print(mes.decode())
    ser.close()