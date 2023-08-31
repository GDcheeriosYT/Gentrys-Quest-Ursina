import json
from ursina import *

music_volume = 1
sound_volume = 1
play_intro = True
hide_fps = False
borderless = False
fullscreen = True
server = "https://gdcheerios.com"
extra_ui_info = True
discord_presence = False
random_pitch_range = (0.7, 1.3)
local_dev_branch = False
fade_time = 0.6
window_position = 0, 0
window_ratio = 1.333


def update_config(settings: dict):
    try:
        # audio
        global music_volume
        global sound_volume
        music_volume = settings["audio"]["music volume"]
        sound_volume = settings["audio"]["sound volume"]

        # graphics
        global hide_fps
        global fullscreen
        global borderless
        global extra_ui_info
        global window_position
        global window_ratio
        hide_fps = settings["graphics"]["hide fps"]
        fullscreen = settings["graphics"]["fullscreen"]
        borderless = settings["graphics"]["borderless"]
        extra_ui_info = settings["graphics"]["extra ui info"]
        window_position = settings["cache"]["window position"][0], settings["cache"]["window position"][1]
        window_ratio = settings["cache"]["window ratio"]
        print("Updated Config!")
    except KeyError:
        print("There was an error updating configuration...")
        print("Resetting settings... T_T")
        save_settings()


def save_settings():
    settings = {
        "audio": {
            "music volume": music_volume,
            "sound volume": sound_volume
        },
        "graphics": {
            "hide fps": hide_fps,
            "fullscreen": fullscreen,
            "borderless": borderless,
            "extra ui info": extra_ui_info
        },
        "cache": {
            "window position": [window.position[0], window.position[1]],
            "window ratio": window.aspect_ratio
        }
    }
    json.dump(settings, open("settings.json", "w+"), indent=4)
    print("Saved Settings!")


def apply_settings():
    window.position = window_position
    window.forced_aspect_ratio = window_ratio
    window.fps_counter.disable() if hide_fps else window.fps_counter.enable()
    window.fullscreen = fullscreen
    print("Applied Settings!")


if os.path.isfile("settings.json"):
    settings = json.load(open("settings.json", "r"))
    update_config(settings)

else:
    save_settings()
