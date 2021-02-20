
class Guild:
    def __init__(self, guild_id, prefix):
        self.id = guild_id
        self.prefix = prefix

    def change_prefix(self, new_prefix):
        self.prefix = new_prefix


class User:
    def __init__(self, user_id, char_sheet):
        self.id = user_id
        self.character = char_sheet

