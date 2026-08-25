import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler


class MacroPad(KMKKeyboard):
    def __init__(self):
        super().__init__()
        self.encoder_handler = EncoderHandler()

        self.encoder_handler.pins = (
            # Encoder 1
            (board.D0, board.D1, None),

            # Encoder 2
            (board.D3, board.D4, None),
        )

        self.encoder_handler.map = [
            (
                # Encoder 1
                (KC.VOLD, KC.VOLU, KC.NO),

                # Encoder 2
                (KC.PREVIOUS_TRACK, KC.NEXT_TRACK, KC.NO),
            ),
        ]
        self.modules.append(self.encoder_handler)
        self.matrix = MatrixScanner(
            row_pins=(board.D6, board.D7),
            column_pins=(board.D8, board.D9, board.D10),
            columns_to_anodes=DiodeOrientation.ROW2COL,
        )
        self.keymap = [
            [
                KC.A, KC.B, KC.C,
                KC.D, KC.E, KC.F,
            ]
        ]


keyboard = MacroPad()

keyboard.go()