import json
from ursina import *

music_volume = 1
sound_volume = 1
play_intro = False
hide_fps = False
borderless = False
fullscreen = True
server = "https://gdcheerios.com"
extra_ui_info = True
discord_presence = False
random_pitch_range = (0.7, 1.3)
local_dev_branch = True
language = "English"
fade_time = 0.6
window_position = 0, 0
window_ratio = 1.333
window_size = 500, 500


def update_config(settings: dict):
    try:
        # language
        global language
        language = settings["language"]

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
        hide_fps = settings["graphics"]["hide fps"]
        fullscreen = settings["graphics"]["fullscreen"]
        borderless = settings["graphics"]["borderless"]
        extra_ui_info = settings["graphics"]["extra ui info"]

        # cache
        global window_position
        global window_ratio
        global window_size
        window_position = settings["cache"]["window position"][0], settings["cache"]["window position"][1]
        window_ratio = settings["cache"]["window ratio"]
        window_size = settings["cache"]["window size"][0], settings["cache"]["window size"][1]
        print("Updated Config!")

    except KeyError:
        print("There was an error updating configuration...")
        print("Resetting settings... T_T")
        save_settings()


def save_settings():
    settings = {
        "language": "English",
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
            "window position": [window_position[0], window_position[1]],
            "window ratio": window_ratio,
            "window size": [window_size[0], window_size[1]]
        }
    }
    json.dump(settings, open("settings.json", "w+"), indent=4)
    print("Saved Settings!")


def apply_settings():
    window.position = window_position
    # window.forced_aspect_ratio = window_ratio
    window.size = window_size
    window.fullscreen = fullscreen
    print("Applied Settings!")


if os.path.isfile("settings.json"):
    settings = json.load(open("settings.json", "r", encoding="utf-8"))
    update_config(settings)

else:
    save_settings()
