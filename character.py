class Character:
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma, hitpoints, def_class, name):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.name = name
        self.weapons = {}
        self.hitpoints = hitpoints
        self.def_class = def_class

    def set_stats(self, hitpoints, def_class):
        self.hitpoints = hitpoints
        self.def_class = def_class

    def add_weapon(self, weapon):
        self.weapons[weapon.name] = weapon

    def attack(self, weapon_name):
        self.weapons[weapon_name].attack()

    def lower_hitpoints(self, attack_hitpoints):
        self.hitpoints = max(0, self.hitpoints - attack_hitpoints)

