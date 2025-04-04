import random

class champion(object):
    def __init__(self, name: str, mirt: bool, vajra: bool, strahd: bool, zariel: bool, elminster: bool, seat: int):
        self.name = name
        self.mirt = mirt
        self.vajra = vajra
        self.strahd = strahd
        self.zariel = zariel
        self.elminster = elminster
        self.seat = seat
    
bruenor = champion("Bruenor", True, True, False, False, False, 1)
deekin = champion("Deekin", False, True, False, False, False, 1)
gale = champion("Gale", False, False, True, False, True, 1)
laezel = champion("Lae'zel", True, True, False, False, True, 2)
widdle = champion("Widdle", False, False, True, False, False, 2)
presto = champion("Presto", True, False, True, False, True, 2)
nayeli = champion("Nayeli", True, True, False, True, False, 3)
gromma = champion("Gromma", False, True, False, True, True, 3)
omin = champion("Omin", False, True, False, False, False, 3)
stoki = champion("Stoki", False, True, True, False, True, 4)
sentry = champion("Sentry", True, True, False, True, False, 4)
karlach = champion("Karlach", True, True, False, True, True, 4)
prudence = champion("Prudence", True, True, True, True, False, 5)
valentine = champion("Valentine", False, True, False, False, True, 5)
briv = champion("Briv", True, True, False, True, False, 5)
asharra = champion("Asharra", False, False, True, True, False, 6)
kas = champion("Kas", True, True, True, True, True, 6)
shandie = champion("Shandie", True, True, True, True, False, 6)

champ_list = [bruenor, deekin, gale, laezel, widdle, presto, nayeli, gromma, omin, stoki, sentry, karlach,
              prudence, valentine, briv, asharra, kas, shandie]
mirt_list = []
vajra_list = []
strahd_list = []
zariel_list = []
elminster_list = []

for champ in champ_list:
    if champ.mirt:
        mirt_list.append(champ)
    if champ.vajra:
        vajra_list.append(champ)
    if champ.strahd:
        strahd_list.append(champ)
    if champ.zariel:
        zariel_list.append(champ)
    if champ.elminster:
        elminster_list.append(champ)

def random_mirt_set(mirt_list):
    chosen_champs = []
    for i in range(3):
        for champ in mirt_list:
            print(f"{champ.name} ", end='')
        print()
        added_champ = random.choice(mirt_list)
        chosen_champs.append(added_champ)
        new_mirt_list = []
        for champ in mirt_list:
            if champ.seat != added_champ.seat:
                new_mirt_list.append(champ)
                mirt_list = new_mirt_list
    for champ in chosen_champs:
        print(f"{champ.name} was chosen to be in the random Mirt set!")

random_mirt_set(mirt_list)