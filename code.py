import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_debouncer import Debouncer

import board
import digitalio

kbd = Keyboard(usb_hid.devices)

button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)

switch = Debouncer(button, interval=0.01)
key = Keycode.F2

state = False

while True:
    switch.update()
    if switch.fell:
        kbd.release(key)
    if switch.rose:
        kbd.press(key)
