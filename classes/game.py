import random


class BColors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

        def disable(self):
            self.HEADER = ''
            self.OKBLUE = ''
            self.OKGREEN = ''
            self.WARNING = ''
            self.FAIL = ''
            self.ENDC = ''


class Person:
    def __init__(self, hp, mp, atk, df, magic):    # health, magic point, attack, defence, magic
        self.maxhp = hp    # hp can change, but it shouldn't go beyond the maximum value
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10    # attack high
        self.df = df
        self.magic = magic    # for dictionary of magic spells
        self.actions = ["Attack", "Magic"]    # to display

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    
