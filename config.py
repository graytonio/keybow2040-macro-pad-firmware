from keymap import LayeredKeyConfig, KeyConfig
from lib.adafruit_hid.keycode import Keycode

KeyConfigs: dict[int, LayeredKeyConfig] = {
    0: LayeredKeyConfig(layers={
        0: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT,
                       Keycode.ALT, Keycode.ZERO],
            released_color=(255, 145, 0),
            pressed_color=(0, 255, 0),
            held_color=(255, 0, 0)
        )
    }),
    1: LayeredKeyConfig(layers={
        0: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT,
                       Keycode.ALT, Keycode.ONE],
            # KeyCodes=[Keycode.A],
            released_color=(255, 255, 255),
            pressed_color=(0, 255, 0),
            held_color=(255, 0, 0)
        ),
        1: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.F],
            # KeyCodes=[Keycode.B],
            released_color=(0, 255, 0),
            pressed_color=(255, 0, 0),
            held_color=(255, 0, 0)
        ),
    }),
    2: LayeredKeyConfig(layers={
        0: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT,
                       Keycode.ALT, Keycode.TWO],
            released_color=(255, 255, 255),
            pressed_color=(0, 255, 0),
            held_color=(255, 0, 0)
        ),
        1: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.G],
            released_color=(0, 255, 0),
            pressed_color=(255, 0, 0),
            held_color=(255, 0, 0)
        ),
    }),
    3: LayeredKeyConfig(layers={
        0: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT,
                       Keycode.ALT, Keycode.THREE],
            released_color=(0, 255, 0),
            pressed_color=(0, 255, 0),
            held_color=(255, 0, 0)
        ),
        1: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.H],
            released_color=(0, 255, 0),
            pressed_color=(255, 0, 0),
            held_color=(255, 0, 0)
        ),
    }),
    4: LayeredKeyConfig(layers={
        0: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT,
                       Keycode.ALT, Keycode.FOUR],
            released_color=(255, 255, 255),
            pressed_color=(0, 255, 0),
            held_color=(255, 0, 0),
        ),
        1: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.I],
            released_color=(0, 255, 0),
            pressed_color=(255, 0, 0),
            held_color=(255, 0, 0)
        ),
    }),
    5: LayeredKeyConfig(layers={
        0: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT,
                       Keycode.ALT, Keycode.FIVE],
            released_color=(255, 255, 255),
            pressed_color=(0, 255, 0),
            held_color=(255, 0, 0)
        ),
        1: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.J],
            released_color=(0, 255, 0),
            pressed_color=(255, 0, 0),
            held_color=(255, 0, 0)
        ),
    }),
    6: LayeredKeyConfig(layers={
        0: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT,
                       Keycode.ALT, Keycode.SIX],
            released_color=(255, 255, 255),
            pressed_color=(0, 255, 0),
            held_color=(255, 0, 0)
        ),
        1: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.K],
            released_color=(0, 255, 0),
            pressed_color=(255, 0, 0),
            held_color=(255, 0, 0)
        ),
    }),
    7: LayeredKeyConfig(layers={
        0: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT,
                       Keycode.ALT, Keycode.SEVEN],
            released_color=(0, 255, 0),
            pressed_color=(0, 255, 0),
            held_color=(255, 0, 0)
        ),
        1: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.L],
            released_color=(0, 255, 0),
            pressed_color=(255, 0, 0),
            held_color=(255, 0, 0)
        ),
    }),
    8: LayeredKeyConfig(layers={
        0: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT,
                       Keycode.ALT, Keycode.EIGHT],
            released_color=(0, 255, 0),
            pressed_color=(0, 255, 0),
            held_color=(255, 0, 0)
        ),
        1: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.M],
            released_color=(0, 255, 0),
            pressed_color=(255, 0, 0),
            held_color=(255, 0, 0)
        ),
    }),
    9: LayeredKeyConfig(layers={
        0: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT,
                       Keycode.ALT, Keycode.ONE],
            released_color=(255, 255, 255),
            pressed_color=(0, 255, 0),
            held_color=(255, 0, 0)
        ),
        1: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.N],
            released_color=(0, 255, 0),
            pressed_color=(255, 0, 0),
            held_color=(255, 0, 0)
        ),
    }),
    10: LayeredKeyConfig(layers={
        0: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT,
                       Keycode.ALT, Keycode.NINE],
            released_color=(255, 255, 255),
            pressed_color=(0, 255, 0),
            held_color=(255, 0, 0)
        ),
        1: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.O],
            released_color=(0, 255, 0),
            pressed_color=(255, 0, 0),
            held_color=(255, 0, 0)
        ),
    }),
    11: LayeredKeyConfig(layers={
        0: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.A],
            released_color=(0, 255, 0),
            pressed_color=(0, 255, 0),
            held_color=(255, 0, 0)
        ),
        1: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.P],
            released_color=(0, 255, 0),
            pressed_color=(255, 0, 0),
            held_color=(255, 0, 0)
        ),
    }),
    12: LayeredKeyConfig(layers={
        0: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.B],
            released_color=(0, 0, 255),
            pressed_color=(0, 255, 0),
            held_color=(255, 0, 0)
        ),
        1: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.Q],
            released_color=(0, 255, 0),
            pressed_color=(255, 0, 0),
            held_color=(255, 0, 0)
        ),
    }),
    13: LayeredKeyConfig(layers={
        0: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.C],
            released_color=(255, 255, 255),
            pressed_color=(0, 255, 0),
            held_color=(255, 0, 0)
        ),
        1: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.R],
            released_color=(0, 255, 0),
            pressed_color=(255, 0, 0),
            held_color=(255, 0, 0)
        ),
    }),
    14: LayeredKeyConfig(layers={
        0: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.D],
            released_color=(255, 255, 255),
            pressed_color=(0, 255, 0),
            held_color=(255, 0, 0)
        ),
        1: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.S],
            released_color=(0, 255, 0),
            pressed_color=(255, 0, 0),
            held_color=(255, 0, 0)
        ),
    }),
    15: LayeredKeyConfig(layers={
        0: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.E],
            released_color=(0, 0, 255),
            pressed_color=(0, 255, 0),
            held_color=(255, 0, 0)
        ),
        1: KeyConfig(
            key_codes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.T],
            released_color=(0, 255, 0),
            pressed_color=(255, 0, 0),
            held_color=(255, 0, 0)
        ),
    })
}
