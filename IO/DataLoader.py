import json
import Game
from Entity.Buff import Buff


class DataLoader:
    @staticmethod
    def parse_characters(character_list_json) -> list:
        characters = []

        for character in character_list_json:
            characters.append(DataLoader.parse_character(character))

        return characters

    @staticmethod
    def parse_character(character_json):
        character = Game.content_manager.get_character(character_json["name"])
        if character_json['equips']['weapon'] is not None:
            character.swap_weapon(DataLoader.parse_weapon(character_json['equips']['weapon']))

        for i in range(5):
            if character_json['equips']['artifacts'][i] is not None:
                character.set_artifact(DataLoader.parse_artifact(character_json['equips']['artifacts'][i]), i)

        character.experience.level = character_json['experience']['level']
        character.experience.xp = character_json['experience']['xp']

        character.update_stats()
        character.stats.health.calculate_value()

        return character

    @staticmethod
    def parse_weapons(weapon_list_json) -> list:
        weapons = []

        for weapon in weapon_list_json:
            weapons.append(DataLoader.parse_weapon(weapon))

        return weapons

    @staticmethod
    def parse_weapon(weapon_json):
        weapon = Game.content_manager.get_weapon(weapon_json['name'])
        weapon.experience.level = weapon_json["experience"]["level"]
        weapon.experience.xp = weapon_json["experience"]["xp"]
        weapon.buff = DataLoader.parse_buff(weapon_json['buff'])

        weapon.update_stats()

        return weapon

    @staticmethod
    def parse_artifacts(artifact_list_json) -> list:
        artifacts = []

        for artifact in artifact_list_json:
            artifacts.append(DataLoader.parse_artifact(artifact))

        return artifacts

    @staticmethod
    def parse_artifact(artifact_json):
        attributes = [DataLoader.parse_buff(attribute) for attribute in artifact_json['stats']['attributes']]
        artifact = Game.content_manager.get_artifact(name=artifact_json['name'], star_rating=artifact_json['star rating'])
        artifact.experience.xp = artifact_json['experience']['xp']
        artifact.experience.level = artifact_json['experience']['level']
        artifact.set_main_attribute(DataLoader.parse_buff(artifact_json['stats']['main attribute']))
        artifact.set_attributes(attributes)
        artifact.set_star_rating(artifact_json['star rating'])

        return artifact

    @staticmethod
    def parse_buff(buff_json):
        buff = Buff(buff_json['stat'], buff_json['is percent'])
        buff.level = buff_json['level']
        return buff
