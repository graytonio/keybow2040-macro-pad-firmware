import usb_hid
from lib.pmk.platform.keybow2040 import Keybow2040 as Hardware
from lib.pmk import PMK, Key
from lib.adafruit_hid.keyboard import Keyboard
from lib.adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


class KeyConfig:
    '''Defines the configuration of a key'''

    def __init__(self, key_codes: list[int], released_color: tuple[int, int, int], pressed_color: tuple[int, int, int], held_color: tuple[int, int, int]):
        self.key_codes = key_codes
        self.released_color = released_color
        self.pressed_color = pressed_color
        self.held_color = held_color


class LayeredKeyConfig:
    '''Defines several key configurations for a given layer'''

    def __init__(self, layers: dict[int, KeyConfig]):
        self.layers = layers

    def has_layer(self, layer: int) -> bool:
        '''Checks if the layer exists in the configuration'''
        return layer in self.layers.keys()


class MacroBoardConfig:
    '''Defines a full interations with the macro board'''

    def __init__(self, key_layers: dict[int, LayeredKeyConfig], led_sleep=False, led_sleep_time=60):
        self.hardware = PMK(Hardware())
        self.keys = self.hardware.keys
        self.keyboard = Keyboard(usb_hid.devices)
        self.layout = KeyboardLayoutUS(self.keyboard)

        self.layer = 0
        self.key_layers = key_layers
        self.hardware.led_sleep_enabled = led_sleep
        self.hardware.led_sleep_time = led_sleep_time
        self.initialize_key_map()

    def update(self):
        '''Updates the key states of the hardware'''
        self.hardware.update()

    def set_layer(self, layer: int):
        '''Sets the layer and updates the keyboard lights to match'''
        self.layer = layer
        self.update_layer()

    def send_key_strokes(self, key_code: int):
        '''Send the keystrokes of the given key for the current layer.  If no key is configured nothing is sent'''
        if not self.key_layers[key_code].has_layer(self.layer):
            return

        # If configured as a single key press
        if all(isinstance(x, int) for x in self.key_layers[key_code].layers[self.layer].key_codes):
            self.keyboard.send(*self.key_layers[key_code].layers[self.layer].key_codes)
            return

        # If configured as series of key presses
        for key_codes in self.key_layers[key_code].layers[self.layer].key_codes:
            self.keyboard.send(*key_codes)
            time.sleep(0.001)

    def set_key_released_color(self, key_code: int):
        '''Sets the given key to the led pattern for released. If no led pattern is configured the led is set to (255, 255, 255)'''
        if not self.key_layers[key_code].has_layer(self.layer):
            self.keys[key_code].set_led(255, 255, 255)
            return

        self.keys[key_code].set_led(
            *self.key_layers[key_code].layers[self.layer].released_color)

    def set_key_pressed_color(self, key_code: int):
        '''Sets the given key to the led pattern for pressed. If no led pattern is configured the led is set to (255, 0, 0)'''
        if not self.key_layers[key_code].has_layer(self.layer):
            self.keys[key_code].set_led(255, 0, 0)
            return

        self.keys[key_code].set_led(
            *self.key_layers[key_code].layers[self.layer].pressed_color)

    def set_key_held_color(self, key_code: int):
        '''Sets the given key to the led pattern for pressed. If no led pattern is configured the led is set to (0, 255, 0)'''
        if not self.key_layers[key_code].has_layer(self.layer):
            self.keys[key_code].set_led(0, 255, 0)
            return

        self.keys[key_code].set_led(
            *self.key_layers[key_code].layers[self.layer].held_color)

    def update_layer(self):
        '''Updates the led states of all keys. Expensive operation should only be called when necessary'''
        for key in self.keys:
            if key.held and key.pressed:
                self.set_key_held_color(key.get_number())
            elif key.pressed:
                self.set_key_pressed_color(key.get_number())
            else:
                self.set_key_released_color(key.get_number())

    def initialize_key_map(self):
        '''Sets up event handlers for all keys'''
        for key_num in self.key_layers:
            @self.hardware.on_release(self.keys[key_num])
            def rising_handler(key: Key):
                if key.held:
                    self.set_layer(0)
                else:
                    self.send_key_strokes(key.get_number())
                    self.set_key_released_color(key.get_number())

            @self.hardware.on_press(self.keys[key_num])
            def falling_handler(key: Key):
                self.set_key_pressed_color(key.get_number())

            @self.hardware.on_hold(self.keys[key_num])
            def hold_handler(key: Key):
                self.set_layer(key.get_number() + 1)

        self.update_layer()
