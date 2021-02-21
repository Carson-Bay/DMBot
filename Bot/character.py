class Attack:

    def __init__(self, name, atk_bonus, damage, other_descriptions):
        self.name = name
        self.atk_bonus = atk_bonus
        self.damage = damage
        self.other_descriptions = descriptions

    def __str__(self):

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

class Character:

    def __init__(self):
        self.name = ""
        self.chara_class = ""
        self.level = 1
        self.background = ""
        self.player_name = ""
        self.race = ""
        self.alignment = ""
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

        self.languages = {}
        self.proficiencies = {}
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

    def __str__(self):
        # Character sheet

        # returns str of character stats

        #Hit_dice = hit_dice.sides in str so hit_dice must not be none

        #Is death save successs/fail supposed to be printed like that


        chara_str = 'Name: {} \
                    \nClass: {} \
                    \nLevel: {}\
                    \nBackground: {}\
                    \nPlayer Name: {}\
                    \nRace: {}\
                    \nExp: {} \
                    \n\nStrength: {} Mod: {} Save: {}\
                    \nDexterity: {} Mod: {} Save: {}\
                    \nConstitution: {} Mod: {} Save: {}\
                    \nIntelligence: {} Mod: {} Save: {}\
                    \nWisdom: {} Mod: {} Save: {}\
                    \nCharisma: {} Mod: {} Save: {}\
                    \n\nInspiration: {}\
                    \nProficiency Bonus: {}\
                    \nPassive Perception: {}\
                    \n\nLanguages:  {}\
                    \nProficiencies: {}\
                    \nOther Proficiencies: {} \
                    \n\nCurrency: \
                    \nCP: {}\
                    \nSP: {}\
                    \nEP: {}\
                    \nGP: {}\
                    \nPP: {} \
                    \n\nInventory: {}\
                    \nAttacks: {}\
                    \nOther Attacks: {}\
                    \n\nInitiative Modifier: {}\
                    \nSpeed: {}\
                    \nHit Dice: {}\
                    \nMax HP: {}\
                    \nCurrent HP: {}\
                    \nDeath Save Successes: {}\
                    \nDeath Save Failures: {}\
                    \n\nFeatures: {}\
                    \n\nPersonality Trait: {}\
                    \nIdeals: {}\
                    \nBonds: {}\
                    \nFlaws: {}' \
            .format(self.name, self.chara_class, self.level, self.background, self.player_name, self.race,
                    self.exp,
                    self.str, self.str_mod, self.str_save, self.dex, self.dex_mod, self.dex_save, self.con,
                    self.con_mod, self.con_save,
                    self.int, self.int_mod, self.int_save, self.wis, self.wis_mod, self.wis_save, self.cha,
                    self.cha_mod, self.cha_save,
                    self.inspiration, self.proficiency_bonus, self.passive_perception,
                    str([*self.languages.values()]).replace("'", '').replace('[', '').replace(']', ''),
                    str([*self.proficiencies.values()]).replace("'", '').replace('[', '').replace(']', ''),
                    str([*self.other_proficiencies.values()]).replace("'", '').replace('[', '').replace(']', '')
                    , self.currency[0],
                    self.currency[1], self.currency[2], self.currency[3], self.currency[4],
                    str([*self.inventory.values()]).replace("'", '').replace('[', '').replace(']', ''),
                    str([*self.attacks.values()]).replace("'", '').replace('[', '').replace(']', ''),
                    str([*self.other_attacks.values()]).replace("'", '').replace('[', '').replace(']', ''),
                    self.initiative_modifier, self.speed, self.hit_dice.sides, self.max_hp, self.current_hp,
                    self.death_save_success, self.death_save_failure,
                    str([*self.features.values()]).replace("'", '').replace('[', '').replace(']', ''),
                    self.personality_trait, self.ideals, self.bonds, self.flaws)

        return chara_str


if __name__ == '__main__':
    c = Character()
    c.hit_dice = Dice(1, 2)
    c.features['beans'] = 'burger'
    c.features['slurp'] = 'schlorp'
    c.languages['slurp'] = 'schlorp'
    c.languages['gchgccc'] = 'schlorp'
    print(str(c))
