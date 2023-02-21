# type: ignore
# from pmk.platform.keybow2040 import Keybow2040 as Hardware
# from pmk import PMK, Key

# import usb_hid
# from adafruit_hid.keyboard import Keyboard
# from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
# from adafruit_hid.keycode import Keycode

import keymap
import config

# pmk = PMK(Hardware())
# pmk.led_sleep_enabled = True  # Allow leds to go to sleep if not being used
# pmk.led_sleep_time = 60  # Time in seconds before keys go to sleep
# keys = pmk.keys

# keyboard = Keyboard(usb_hid.devices)
# layout = KeyboardLayoutUS(keyboard)


# def set_key_pressed_color(key_code: int):
#     if not config.KeyConfigs[key_code].has_layer(keymap.LAYER):
#         keys[key_code].set_led(255, 0, 255)  # By default pressed keys are red
#         return

#     keys[key_code].set_led(
#         *config.KeyConfigs[key_code].layers[keymap.LAYER].PressedColor)


# def set_key_released_color(key_code: int):
#     if not config.KeyConfigs[key_code].has_layer(keymap.LAYER):
#         # By default released keys are white
#         keys[key_code].set_led(255, 255, 255)
#         return

#     keys[key_code].set_led(
#         *config.KeyConfigs[key_code].layers[keymap.LAYER].ReleasedColor)


# def set_key_held_color(key_code: int):
#     if not config.KeyConfigs[key_code].has_layer(keymap.LAYER):
#         keys[key_code].set_led(0, 0, 255)  # By default held keys are green
#         return

#     keys[key_code].set_led(
#         *config.KeyConfigs[key_code].layers[keymap.LAYER].HeldColor)


# def send_key_strokes(key_code: int):
#     if not config.KeyConfigs[key_code].has_layer(keymap.LAYER):
#         return  # By default send no keycodes

#     keyboard.send(*config.KeyConfigs[key_code].layers[keymap.LAYER].KeyCodes)


# def update_layer():
#     for key in keys:
#         if key.is_held() and key.pressed:
#             set_key_held_color(key.get_number())
#         elif key.pressed:
#             set_key_pressed_color(key.get_number())
#         else:
#             set_key_released_color(key.get_number())


# def set_layer(layer: int):
#     keymap.LAYER = layer
#     update_layer()


# for key_num, config in config.KeyConfigs.items():
#     @pmk.on_release(keys[key_num])
#     def rising_handler(key: Key):
#         # If you were holding a layer key reset the layer
#         if key.is_held():
#             set_layer(0)
#         else:
#             send_key_strokes(key.get_number())
#             set_key_released_color(key.get_number())

#     @pmk.on_press(keys[key_num])
#     def falling_handler(key: Key):
#         set_key_pressed_color(key.get_number())

#     @pmk.on_hold(keys[key_num])
#     def hold_handler(key: Key):
#         set_layer(key.get_number() + 1)

#     update_layer()

keyboard = keymap.MacroBoardConfig(key_layers=config.KeyConfigs)

while True:
    keyboard.update()
