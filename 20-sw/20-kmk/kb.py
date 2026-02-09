import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        super().__init__()

        self.row_pins = (
            board.D29,              # top row
            board.D28,
            board.D27,
            board.D26,
            board.SCK, # D22
            board.MISO, # D20       # bottom row
        )

        self.col_pins = (
            board.MOSI, # D23       # left column

            board.D21,
            board.D16,
            board.D15,
            board.D14,

            board.D13,
            board.D12,
            # board.D9, # This is a natural pinout (in the corner) for the wire, but I destroyed the pinout
            board.D10, # This a pinout I converted from GND by cutting the jumper (It's 4th from the UCB-C)
            board.D8,

            board.D7,
            board.D6,
            board.D5,
            board.D4,
            
            board.D3,
            board.D2,
            board.RX, # D1
            board.TX, # D0          # right column
        )

        self.diode_orientation = DiodeOrientation.COL2ROW

        # fmt: off
        self.coord_mapping = [
           0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
          17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 
          34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 
          51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,     66, 67, 
          68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 
          85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,100,101
        ] 
        # fmt: on
