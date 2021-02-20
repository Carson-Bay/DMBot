from enum import IntEnum

class Attack:

    def __init__(self, name, atk_bonus, damage, other_descriptions):
        self.name = name
        self.atk_bonus = atk_bonus
        self.damage = damage
        self.other_descriptions = descriptions

    def __str__(self):
        # TODO
        pass

class Description:
    
    def __init__(self, title, description):
        self.title = title
        self.description = description

class Dice:

    def __init__(self, amount, sides):
        self.amount = amount
        self.sides = sides

    def roll(self):
        result = [];
        for i in range(0, amount):
            result.append(random.randint(1, sides))
        return result

class CharacterCompletion(IntEnum):
    START = 0
    NAME = 1
    RACE = 2
    CLASS = 3
    BACKGROUND = 4
    ALIGNMENT = 5
    LEVEL = 6
    EXP = 7
    STR = 8
    DEX = 9
    CON = 10
    INT = 11
    WIS = 12
    CHA = 13
    MODS = 14
    SAVES = 15
    INSPIRATION = 16
    PROFICIENCY_MODIFIER = 17
    SKILLS = 18
    PROFICIENCIES = 19
    LANGUAGES = 20
    OTHER_PROFICIENCIES = 21
    CURRENCY = 22
    EQUIPMENT = 23
    ATTACKS = 24
    OTHER_ATTACKS = 24
    ARMOR_CLASS = 25
    INITIATIVE = 26
    SPEED = 27
    HIT_DICE = 28
    MAX_HP = 29
    HP = 30
    DEATH_SAVES = 31
    FEATURES = 32
    PERSONALITY = 33
    IDEALS = 34
    BONDS = 35
    FLAWS = 36
    FINISH = 37

class Character:

    def __init__(self):
        self.name = ""
        self.race = ""
        self.chara_class = ""
        self.background = ""
        self.alignment = ""

        self.level = 1
        self.exp = 0

        self.str = 0
        self.dex = 0
        self.con = 0
        self.int = 0
        self.wis = 0
        self.cha = 0
        self.str_mod = 0
        self.dex_mod = 0
        self.con_mod = 0
        self.int_mod = 0
        self.wis_mod = 0
        self.cha_mod = 0
        self.str_save = 0
        self.dex_save = 0
        self.con_save = 0
        self.int_save = 0
        self.wis_save = 0
        self.cha_save = 0

        self.inspiration = 0
        self.proficiency_bonus = 0
        self.passive_perception = 0
        self.skills = {
            "Acrobatics": 0
            "Animal Handling": 0
            "Arcana": 0
            "Athletics": 0
            "Deception": 0
            "History": 0
            "Insight": 0
            "Intimidation": 0
            "Investigation": 0
            "Medicine": 0
            "Nature": 0
            "Perception": 0
            "Performance": 0
            "Persuasion": 0
            "Religion": 0
            "Sleight of Hand": 0
            "Stealth": 0
            "Survival": 0
        }
        
        self.proficiencies = {}
        self.languages = {}
        self.other_proficiencies = {} # set of Description

        self.currency = [0, 0, 0, 0, 0] # CP, SP, EP, GP, PP
        self.inventory = {}

        self.attacks = {}
        self.other_attacks = {} # set of Description

        self.armor_class = 0
        self.initiative_modifier = self.dex_mod
        self.speed = 0
        self.hit_dice = None # Dice object
        self.max_hp = 0
        self.current_hp = self.max_hp
        self.temp_hp = 0
        self.death_save_success = 0
        self.death_save_failure = 0

        self.features = {} # set of Description

        self.personality_trait = ""
        self.ideals = ""
        self.bonds = ""
        self.flaws = ""

        self.creation_progress = CharacterCompletion.START
        self.confirmation = False

    def continue_create(self, input):
        if self.creation_progress == CharacterCompletion.START:
            if self.confirmation: # this is the confirmation message
                if input == "y" || input == "yes":
                    # proceed
                else:
                    # reject
            else:

                # send confirm message

    def __str__(self):
        # Character sheet
        pass
