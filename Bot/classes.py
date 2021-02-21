import discord


class Guild:
    def __init__(self, guild_id, prefix):
        self.id = guild_id
        self.prefix = prefix

    def change_prefix(self, new_prefix):
        self.prefix = new_prefix


class User:
    def __init__(self, user_id, char_sheet: list):
        self.id = user_id
        self.character = char_sheet

    def add_char_sheet(self, sheet):
        self.character.append(sheet)


class Session:
    def __init__(self, guild_id):
        self.id = guild_id
        self.characters = None
