from kb import KMKKeyboard

from kmk.keys import KeyboardKey, make_key
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())

APP_KEY = make_key(names=('APP', 'MENU'), constructor=KeyboardKey, code=101)

# fmt: off
keyboard.keymap = [
    [  # BASE
        KC.ESC,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,                                       KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,      KC.PSCR, KC.SLCK, KC.PAUS, KC.INS,
        KC.BRIU ,KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,                     KC.VOLD, KC.VOLU,                   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS,     KC.EQL,  KC.RBRC, KC.BSPC, KC.MUTE,
        KC.BRID, KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R ,            KC.N5,                     KC.N6,   KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC,              KC.BSLS, KC.F18,KC.HOME,
                 KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.T,    KC.MPLY,                   KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,                       KC.ENT,  KC.END, 
                 KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,             KC.MPRV, KC.MNXT,          KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT,              KC.PGUP, KC.UP,   KC.PGDN,
                 KC.LCTL, KC.F13,  KC.F14,  KC.F15,  KC.LGUI, KC.LALT,          KC.SPC,  KC.ENT,           KC.RALT, KC.RGUI, KC.APP,  KC.F16,  KC.F17,  KC.RCTL,              KC.LEFT, KC.DOWN, KC.RGHT
    ],
]
# fmt: on

if __name__ == '__main__':
    keyboard.go()
