from keymap import LayeredKeyConfig, KeyConfig
from adafruit_hid.keycode import Keycode

KeyConfigs: dict[int, LayeredKeyConfig] = {
    0: LayeredKeyConfig(layers={
        0: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT,
                      Keycode.ALT, Keycode.ZERO],
            ReleasedColor=(255, 145, 0),
            PressedColor=(0, 255, 0),
            HeldColor=(255, 0, 0)
        )
    }),
    1: LayeredKeyConfig(layers={
        0: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT,
                      Keycode.ALT, Keycode.ONE],
            # KeyCodes=[Keycode.A],
            ReleasedColor=(255, 255, 255),
            PressedColor=(0, 255, 0),
            HeldColor=(255, 0, 0)
        ),
        1: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.F],
            # KeyCodes=[Keycode.B],
            ReleasedColor=(0, 255, 0),
            PressedColor=(255, 0, 0),
            HeldColor=(255, 0, 0)
        ),
    }),
    2: LayeredKeyConfig(layers={
        0: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT,
                      Keycode.ALT, Keycode.TWO],
            ReleasedColor=(255, 255, 255),
            PressedColor=(0, 255, 0),
            HeldColor=(255, 0, 0)
        ),
        1: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.G],
            ReleasedColor=(0, 255, 0),
            PressedColor=(255, 0, 0),
            HeldColor=(255, 0, 0)
        ),
    }),
    3: LayeredKeyConfig(layers={
        0: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT,
                      Keycode.ALT, Keycode.THREE],
            ReleasedColor=(0, 255, 0),
            PressedColor=(0, 255, 0),
            HeldColor=(255, 0, 0)
        ),
        1: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.H],
            ReleasedColor=(0, 255, 0),
            PressedColor=(255, 0, 0),
            HeldColor=(255, 0, 0)
        ),
    }),
    4: LayeredKeyConfig(layers={
        0: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT,
                      Keycode.ALT, Keycode.FOUR],
            ReleasedColor=(255, 255, 255),
            PressedColor=(0, 255, 0),
            HeldColor=(255, 0, 0),
        ),
        1: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.I],
            ReleasedColor=(0, 255, 0),
            PressedColor=(255, 0, 0),
            HeldColor=(255, 0, 0)
        ),
    }),
    5: LayeredKeyConfig(layers={
        0: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT,
                      Keycode.ALT, Keycode.FIVE],
            ReleasedColor=(255, 255, 255),
            PressedColor=(0, 255, 0),
            HeldColor=(255, 0, 0)
        ),
        1: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.J],
            ReleasedColor=(0, 255, 0),
            PressedColor=(255, 0, 0),
            HeldColor=(255, 0, 0)
        ),
    }),
    6: LayeredKeyConfig(layers={
        0: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT,
                      Keycode.ALT, Keycode.SIX],
            ReleasedColor=(255, 255, 255),
            PressedColor=(0, 255, 0),
            HeldColor=(255, 0, 0)
        ),
        1: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.K],
            ReleasedColor=(0, 255, 0),
            PressedColor=(255, 0, 0),
            HeldColor=(255, 0, 0)
        ),
    }),
    7: LayeredKeyConfig(layers={
        0: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT,
                      Keycode.ALT, Keycode.SEVEN],
            ReleasedColor=(0, 255, 0),
            PressedColor=(0, 255, 0),
            HeldColor=(255, 0, 0)
        ),
        1: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.L],
            ReleasedColor=(0, 255, 0),
            PressedColor=(255, 0, 0),
            HeldColor=(255, 0, 0)
        ),
    }),
    8: LayeredKeyConfig(layers={
        0: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT,
                      Keycode.ALT, Keycode.EIGHT],
            ReleasedColor=(0, 255, 0),
            PressedColor=(0, 255, 0),
            HeldColor=(255, 0, 0)
        ),
        1: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.M],
            ReleasedColor=(0, 255, 0),
            PressedColor=(255, 0, 0),
            HeldColor=(255, 0, 0)
        ),
    }),
    9: LayeredKeyConfig(layers={
        0: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT,
                      Keycode.ALT, Keycode.ONE],
            ReleasedColor=(255, 255, 255),
            PressedColor=(0, 255, 0),
            HeldColor=(255, 0, 0)
        ),
        1: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.N],
            ReleasedColor=(0, 255, 0),
            PressedColor=(255, 0, 0),
            HeldColor=(255, 0, 0)
        ),
    }),
    10: LayeredKeyConfig(layers={
        0: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT,
                      Keycode.ALT, Keycode.NINE],
            ReleasedColor=(255, 255, 255),
            PressedColor=(0, 255, 0),
            HeldColor=(255, 0, 0)
        ),
        1: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.O],
            ReleasedColor=(0, 255, 0),
            PressedColor=(255, 0, 0),
            HeldColor=(255, 0, 0)
        ),
    }),
    11: LayeredKeyConfig(layers={
        0: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.A],
            ReleasedColor=(0, 255, 0),
            PressedColor=(0, 255, 0),
            HeldColor=(255, 0, 0)
        ),
        1: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.P],
            ReleasedColor=(0, 255, 0),
            PressedColor=(255, 0, 0),
            HeldColor=(255, 0, 0)
        ),
    }),
    12: LayeredKeyConfig(layers={
        0: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.B],
            ReleasedColor=(0, 0, 255),
            PressedColor=(0, 255, 0),
            HeldColor=(255, 0, 0)
        ),
        1: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.Q],
            ReleasedColor=(0, 255, 0),
            PressedColor=(255, 0, 0),
            HeldColor=(255, 0, 0)
        ),
    }),
    13: LayeredKeyConfig(layers={
        0: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.C],
            ReleasedColor=(255, 255, 255),
            PressedColor=(0, 255, 0),
            HeldColor=(255, 0, 0)
        ),
        1: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.R],
            ReleasedColor=(0, 255, 0),
            PressedColor=(255, 0, 0),
            HeldColor=(255, 0, 0)
        ),
    }),
    14: LayeredKeyConfig(layers={
        0: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.D],
            ReleasedColor=(255, 255, 255),
            PressedColor=(0, 255, 0),
            HeldColor=(255, 0, 0)
        ),
        1: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.S],
            ReleasedColor=(0, 255, 0),
            PressedColor=(255, 0, 0),
            HeldColor=(255, 0, 0)
        ),
    }),
    15: LayeredKeyConfig(layers={
        0: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.E],
            ReleasedColor=(0, 0, 255),
            PressedColor=(0, 255, 0),
            HeldColor=(255, 0, 0)
        ),
        1: KeyConfig(
            KeyCodes=[Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.T],
            ReleasedColor=(0, 255, 0),
            PressedColor=(255, 0, 0),
            HeldColor=(255, 0, 0)
        ),
    })
}
