import os
import json

import Game

volume = 1
play_intro = False
hide_fps = False
borderless = False
fullscreen = True
server = "https://gdcheerios.com"
debug = False
extra_ui_info = True
random_pitch_range = (0.7, 1.3)
local_dev_branch = False
fade_time = 0.6


def update_config(settings: dict):
    # audio
    global volume
    volume = settings["audio"]["volume"]

    # graphics
    global hide_fps
    global fullscreen
    global borderless
    global extra_ui_info
    hide_fps = settings["graphics"]["hide fps"]
    fullscreen = settings["graphics"]["fullscreen"]
    borderless = settings["graphics"]["borderless"]
    extra_ui_info = settings["graphics"]["extra ui info"]


def save_settings():
    settings = {
        "audio": {
            "volume": volume
        },
        "graphics": {
            "hide fps": hide_fps,
            "fullscreen": fullscreen,
            "borderless": borderless,
            "extra ui info": extra_ui_info
        }
    }
    json.dump(settings, open("settings.json", "w+"), indent=4)


def apply_settings():
    Game.window.fps_counter.disable() if hide_fps else Game.window.fps_counter.enable()
    Game.window.fullscreen = fullscreen

    save_settings()


if os.path.isfile("settings.json"):
    settings = json.load(open("settings.json", "r"))
    update_config(settings)

else:
    save_settings()
