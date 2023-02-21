# Keybow 2040 Macro Pad Firmware

This is firmware made for the [Pimoroni Keybow 2040](https://shop.pimoroni.com/products/keybow-2040). It implements the functionality I wanted out of it will full customizability and several layer functions.

## Main features

- Fully customizable key codes for each key
- 17 Layers for a total of 241 keys to press
- Individual lighting control with settings for pressed, released, and held.

## Future Features

- [ ] Serial communication. Purpose TBD
- [ ] Mutli Key Cords
- [ ] Makefile auto discover board directory

## Configuration

To configure the firmware first clone the project then rename the `config.py.example` to `config.py`. This file is now where you can configure how you want each key and layer to operate.

The top level dictionary entry is the key index. On the keybow 2040 the keys are indexed from the bottom left as 0 going up the column to 3 then 4 is the second from the left on the bottom etc. The key entry contains a set of layers with individual key configurations where each entry is a layer number. The default layer is 0 and whenever a key is held the keyboard is switched to layer that keys index + 1. So for example if you held down the 0 index key you will be brought to layer 1. The following config example has been commented to help you understand the key configurations.

```python3
KeyConfigs: dict[int, LayeredKeyConfig] = {
    0: LayeredKeyConfig(layers={                            # Configuration for the key at index 0
        0: KeyConfig(                                       # Configuration for layer 0
            key_codes=[Keycode.CONTROL, Keycode.SHIFT,      # Key codes to be sent when the key is pressed
                       Keycode.ALT, Keycode.ZERO],
            released_color=(255, 255, 255),                 # LED pattern when the key is not pressed or held
            pressed_color=(255, 0, 0),                      # LED pattern when the key is pressed but not held
            held_color=(0, 0, 255)                          # LED pattern when the key is held
        )
    }),
}
```

## Uploading

To upload your code to the board, assuming you are using is running CircuitPython. You can either copy all the files to the board manually or you can configure the Makefile to point towards where the CIRCUITPY drive is mounted on your computer then use `make upload`.
