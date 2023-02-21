import usb_hid
from adafruit_hid.keycode import Keycode
from pmk.platform.keybow2040 import Keybow2040 as Hardware
from pmk import PMK, Key
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


class KeyConfig:
    def __init__(self, KeyCodes: list[int], ReleasedColor: tuple[int, int, int], PressedColor: tuple[int, int, int], HeldColor: tuple[int, int, int], Cords: dict[int, list[int]] = {}):
        self.KeyCodes = KeyCodes
        self.ReleasedColor = ReleasedColor
        self.PressedColor = PressedColor
        self.HeldColor = HeldColor
        # Mapping held keys with this key to a key combo only supports 2 key cords
        self.Cords = Cords


class LayeredKeyConfig:
    def __init__(self, layers: dict[int, KeyConfig]):
        self.layers = layers

    def has_layer(self, layer: int) -> bool:
        return layer in self.layers.keys()


class MacroBoardConfig:
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
        self.hardware.update()

    def set_layer(self, layer: int):
        self.layer = layer
        self.update_layer()

    def send_key_strokes(self, key_code: int):
        if not self.key_layers[key_code].has_layer(self.layer):
            return

        self.keyboard.send(
            *self.key_layers[key_code].layers[self.layer].KeyCodes)

    def set_key_released_color(self, key_code: int):
        if not self.key_layers[key_code].has_layer(self.layer):
            self.keys[key_code].set_led(255, 255, 255)
            return

        self.keys[key_code].set_led(
            *self.key_layers[key_code].layers[self.layer].ReleasedColor)

    def set_key_pressed_color(self, key_code: int):
        if not self.key_layers[key_code].has_layer(self.layer):
            self.keys[key_code].set_led(255, 0, 0)
            return

        self.keys[key_code].set_led(
            *self.key_layers[key_code].layers[self.layer].PressedColor)

    def set_key_held_color(self, key_code: int):
        if not self.key_layers[key_code].has_layer(self.layer):
            self.keys[key_code].set_led(0, 255, 0)
            return

        self.keys[key_code].set_led(
            *self.key_layers[key_code].layers[self.layer].HeldColor)

    def update_layer(self):
        for key in self.keys:
            if key.held and key.pressed:
                self.set_key_held_color(key.get_number())
            elif key.pressed:
                self.set_key_pressed_color(key.get_number())
            else:
                self.set_key_released_color(key.get_number())

    def initialize_key_map(self):
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
