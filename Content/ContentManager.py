# Artifact Families
from Content.ArtifactFamilies.BraydenMesserschmidt.BraydenMesserschmidtFamily import BraydenMesserschmidtFamily
from Content.ArtifactFamilies.TestFamily.TestFamily import TestFamily
from Content.ArtifactFamilies.HyVee.HyVee import HyVee

# Characters
from Content.Characters.StarterCharacter.StarterCharacter import StarterCharacter
from Content.Characters.BraydenMesserschmidt.BraydenMesserschmidt import BraydenMesserschmidt
from Content.Characters.PeteMarks.PeteMarks import PeteMarks
from Content.Characters.PhilipMcClure.PhilipMcClure import PhilipMcClure
from Content.Characters.MasonJames.MasonJames import MasonJames

# Effects
# no effects lol

# Enemies
from Content.Enemies.TestEnemy import TestEnemy
from Content.Enemies.AngryPedestrian.AngryPedestrian import AngryPedestrian
from Content.Enemies.AngryChineseMan.AngryChineseMan import AngryChineseMan

# Locations
from Content.Locations.TestLocation.TestLocation import TestLocation

# Weapon
from Content.Weapons.Knife.Knife import Knife
from Content.Weapons.BraydensOsuPen.BraydensOsuPen import BraydensOsuPen


class ContentManager:
    def __init__(self):
        self.artifact_families = [
            BraydenMesserschmidtFamily,
            TestFamily,
            HyVee
        ]

        self.characters = [
            StarterCharacter,
            BraydenMesserschmidt,
            PeteMarks,
            PhilipMcClure,
            MasonJames
        ]
        
        self.effects = []
        
        self.enemies = [
            TestEnemy,
            AngryPedestrian,
            AngryChineseMan
        ]

        self.locations = [
            TestLocation
        ]

        self.weapons = [
            Knife,
            BraydensOsuPen
        ]

    def get_family(self, name: str):
        for family in self.artifact_families:
            if name == family.name:
                return family()

    def get_character(self, name):
        for character in self.characters:
            if name == character.name:
                return character()

    def get_enemy(self, name):
        for enemy in self.enemies:
            if name == enemy.name:
                return enemy()

    def get_location(self, name):
        for location in self.locations:
            if name == location.name:
                return location()

    def get_weapon(self, name):
        for weapon in self.weapons:
            if name == weapon.name:
                return weapon()
