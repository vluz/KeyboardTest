"""
MacroKey
"""

import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.display import Display, SSD1306, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306

# Pinout
COL1 = board.D0
COL2 = board.D1

ROW1 = board.D2
ROW2 = board.D3

PUSHBUTTON = board.D9
ROTA = board.D7
ROTB = board.D8

NEOPIXEL = board.D10

# Keyboard
keyboard = KMKKeyboard()

# Matrix settings
keyboard.col_pins = (COL1, COL2)
keyboard.row_pins = (ROW1, ROW2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.extensions.append(MediaKeys())

# RGB LEDs settings
rgb_ext = RGB(
    pixel_pin = NEOPIXEL,
    num_pixels = 2,
    hue_default = 100,
    sat_default = 255,
    val_default = 15,
    val_limit = 25,
    animation_speed = 10,
    animation_mode=AnimationModes.RAINBOW,
    refresh_rate = 30,
)
keyboard.extensions.append(rgb_ext)

# Display settings
i2c_bus = busio.I2C(board.SCL, board.SDA)
display_driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

display = Display(
    display=display_driver,
    entries=[
        ImageEntry(image="KBDLOGO1.bmp", x=0, y=0),
    ],
    width=128,
    height=32,
    brightness=0.8,
    brightness_step=0.1,
    dim_time=20,
    dim_target=0.1,
    off_time=120,
    powersave_dim_time=10,
    powersave_dim_target=0.1,
    powersave_off_time=30,
)
keyboard.extensions.append(display)

# Encoder settings
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((ROTA, ROTB, PUSHBUTTON, False),)
encoder_handler.map = (((KC.VOLD, KC.VOLU, KC.MUTE),),)

# Keymap
keyboard.keymap = [
    [KC.LCTRL(KC.C), KC.LCTRL(KC.V),
    KC.A, KC.Z,
    ]
]

if __name__ == '__main__':
    keyboard.go()
