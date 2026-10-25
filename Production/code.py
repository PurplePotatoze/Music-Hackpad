import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
media_keys = MediaKeys()
macros = Macros() 

keyboard.modules = [encoder_handler]
keyboard.extensions.append(media_keys)

keyboard.row_pins = (board.D6, board.D7)
keyboard.col_pins = (board.D8, board.D9, board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 4. Map the physical rotary encoders (Pins A, B, Click)
encoder_handler.pins = (
    # Encoder 1 
    (board.D0, board.D1, board.D2),
    # Encoder 2 
    (board.D3, board.D4, board.D5),
)

# 5. Define rotation actions
encoder_handler.map = (
    (
        # Encoder 1: Turn CCW, Turn CW, Press Click
        (KC.VOLD, KC.VOLU, KC.MUTE),
        # Encoder 2: Turn CCW, Turn CW, Press Click
        (KC.MNXT, KC.MPRV, KC.MPLY),
    ),
)

# 6. Map your 6 keys (A to F)
keyboard.keymap = [
    [
        KC.A, KC.B, KC.C,
        KC.D, KC.E, KC.F,
    ]
]

if __name__ == '__main__':
    keyboard.go()