from ursina import *

from typing import Union

import GameConfiguration


class AudioSystem:
    def __init__(self, music_volume: float, sound_volume: float):
        self._music_volume = music_volume
        self._sound_volume = sound_volume
        self._background_music = None
        self._background_music: Audio

    def set_music(self, audio_file: str, play: bool = True):
        """
        Set the music of the game.

        :param audio_file: The path to the audio.
        :param play: If the music should immediately play.
        """

        if self._background_music:
            self._background_music.stop()

        self._background_music = Audio(audio_file, loop=True, autoplay=False)
        if play:
            self._background_music.play()
        else:
            self._background_music.pause()

    def toggle_music_pause(self, fade: bool = True, fade_time: Union[int, bool] = 0.5):
        """
        Pauses and unpauses the game music.

        :param fade: Whether the music should fade in or out or not.
        :param fade_time: The amount of time the fade takes.
        """

        print("is playing", self._background_music.playing)

        if self._background_music.playing == 1:
            if fade:
                self._background_music.volume = self._music_volume
                self._background_music.fade(0, fade_time)
                invoke(self._background_music.pause, delay=fade_time)
            else:
                self._background_music.pause()

        else:
            if fade:
                self._background_music.volume = 0
                self._background_music.resume()
                self._background_music.fade(self._music_volume, fade_time)
            else:
                self._background_music.resume()

    def play_sound(self, sound, randomize_pitch: bool = False):
        """
        Plays a sound.

        :param sound: The sound to be played.
        :param randomize_pitch: Whether the pitch should be randomized.
        """

        if randomize_pitch:
            sound.pitch = random.uniform(GameConfiguration.random_pitch_range[0],
                                         GameConfiguration.random_pitch_range[1])

        sound.volume = self._sound_volume
        sound.play()

    def change_music_volume(self, value: float):
        """
        Change the music volume

        :param value: The volume for the music.
        """

        self._music_volume = value
        if self._background_music:
            self._background_music.volume = self._music_volume

    def change_sound_volume(self, value: float):
        """
        Change the sound volume

        :param value: The volume for the sound.
        """

        self._sound_volume = value
