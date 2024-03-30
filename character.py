from exceptions import UnknownCharacter
from enums import Characters
from relics import RelicsComponent


class Character(object):
    def __init__(self, character: Characters) -> None:
        if character not in Characters:
            raise UnknownCharacter(f"Unknown character: {character}")
        self.character = character
        self.relics = [RelicsComponent() for _ in range(6)]

    def get_character_id(self):
        return self.character.value[0]

    def get_character_name(self):
        return self.character.value[1]

    def set_character(self, character: Characters):
        if character not in Characters:
            raise UnknownCharacter(f"Unknown character: {character}")

        self.character = character

    def __str__(self):
        return f"{self.character.value[1]}"
