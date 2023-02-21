import keymap
import config

keyboard = keymap.MacroBoardConfig(key_layers=config.KeyConfigs)

while True:
    keyboard.update()
