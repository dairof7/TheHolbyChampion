from base import Base

class Champion(Base):

    weapons = {"light_ax":{'Health': 100, 'Attack': 1, 'Defense': 2, 'Magic': 4,  'Speed': 2},
    "celestial_stave": {'Health': 100, 'Attack': 1, 'Defense': 2, 'Magic': 4, 'Speed': 2},
	"spire_of_hakkar": {'Health': 120, 'Attack': 1, 'Defense': 2, 'Magic': 5, 'Speed': 1}}

    armor = {"heavy":{'Health': 400, 'Attack': 0, 'Defense': 7, 'Magic': 0,  'Speed': 2},
    "white_cloth": {'Health': 150, 'Attack': 0, 'Defense': 3, 'Magic': 2, 'Speed': 3},
	"dark_cloth": {'Health': 120, 'Attack': 0, 'Defense': 3, 'Magic': 2, 'Speed': 4}}


    def __init__(self, chclass,hname, race, gender):
        super().__init__(hname, race, gender)
        self.chclass = chclass
        self.create()



    @property
    def chclass(self):
        return self.__chclass

    @chclass.setter
    def chclass(self, chclass):
        lista = {1: 'Cleric', 2: 'Fighter', 3: 'Mage', 4: 'Paladin', 5: 'Ranger', 6: 'Rogue'}
        self.__chclass = lista[chclass]


    def create(self):
        if self.chclass == "Cleric":
            new_stats = {'Health': 100, 'Attack': 1, 'Defense': 2, 'Magic': 4, 'Speed': 2}
            self.weapon = "celestial_stave"
            self.armor = "white_cloth"
        if self.chclass == "Fighter":
            new_stats = {'Health': 200, 'Attack': 4, 'Defense': 3, 'Magic': 1, 'Speed': 3}
            self.weapon = "light_ax"
            self.armor = "heavy"
        if self.chclass == "Mage":
            new_stats = {'Health': 150, 'Attack': 3, 'Defense': 2, 'Magic': 6, 'Speed': 4}
            self.weapon = "spire_of_hakkar"
            self.armor = "dark_cloth"
        if self.chclass == "Paladin":
            new_stats = {'Health': 250, 'Attack': 8, 'Defense': 6, 'Magic': 1, 'Speed': 3}
        if self.chclass == "Ranger":
            new_stats = {'Health': 180, 'Attack': 5, 'Defense': 4, 'Magic': 2, 'Speed': 4}
        if self.chclass == "Rogue":
            new_stats = {'Health': 200, 'Attack': 5, 'Defense': 3, 'Magic': 2, 'Speed': 7}

        for key, value in new_stats.items():
            self.stats[key] = value
        self.setweapon()
        self.setarmor()


    def setweapon(self):
        weapon_stats = Champion.weapons[self.weapon]
        for key, value in weapon_stats.items():
            self.stats[key] += weapon_stats[key]

    def setarmor(self):
        armor_stats = Champion.armor[self.armor]
        for key, value in armor_stats.items():
            self.stats[key] += armor_stats[key]

    def __str__(self):
        string = ""
        for key, value in self.__dict__.items():
            string += key.split("__")[-1] + ": " + str(value) + "\n"
        return string

    @classmethod
    def attack():
        pass

    @classmethod
    def defend():
        pass

    @classmethod
    def useMagic():
        pass