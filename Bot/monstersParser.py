# Monster data taken from http://donjon.bin.sh/5e/monsters/

import pickle

monsters = {}

with open("monsters.txt", "rt") as file:
    for line in file:
        line = line.split("\t")
        monster_name = line[0]
        monster_size = line[1]
        monster_type = line[2]
        monster_tags = line[3]
        monster_alignment = line[4]
        monster_cr = line[5]
        monster_xp = line[6]
        monsters[monster_name] = {"size": monster_size, "type": monster_type,
                                  "tags": monster_tags, "align": monster_alignment,
                                  "cr": monster_cr, "xp": monster_xp}


with open("monsters.pickle", "wb") as file:
    pickle.dump(monsters, file)

