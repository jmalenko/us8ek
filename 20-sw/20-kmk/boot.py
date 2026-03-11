import board
from kmk.bootcfg import bootcfg

# Normally, the keyboard appears as a keyboard.
# When Left Control is pressed during boot, the keyboard also appears as a storage devise, therefore allowing the configuration updates.

bootcfg(
    sense = board.MOSI,  # column
    source = board.MISO, # row
    midi = False,
    mouse = False,
    # storage = False,
    usb_id = {
        'manufacturer': 'JM', 
        'product': 'US8EK: Unibody Split Keyboard with Arrow Keys'},
)