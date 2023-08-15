from random import randint


class Weapon:
    def __init__(self, name, accuracy_bonus, attack_mult, attack_dice,  attack_bonus):
        self.name = name
        self.accuracy_bonus = accuracy_bonus
        self.attack_mult = attack_mult
        self.attack_dice = attack_dice
        self.attack_bonus = attack_bonus

    def attack(self):
        print(randint(1, 20) + self.accuracy_bonus, self.attack_mult*randint(1, self.attack_dice) + self.attack_bonus)