import storage, usb_cdc
from adafruit_debouncer import Debouncer
import board
import digitalio

button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)

switch = Debouncer(button, interval=0.01)

if not switch.value:
    storage.disable_usb_drive()
    usb_cdc.disable()
