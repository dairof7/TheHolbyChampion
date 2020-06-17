#!/usr/bin/python3

"""Module for Square Class"""

class Base:
    nchars = 0

    def __init__(self, hname=1, race=1, gender=1):

        self.hname = hname
        self.race = race
        self.gender = gender
        self.lv = 0
        self.exp = 100
        self.curr_exp = 0
        self.total_exp = 0
        self.stats = {'Health': 100, 'Attack': 0, 'Defense': 0, 'Magic': 0, 'Speed': 0}
        self.stats_p = 0
        Base.nchars += 1



    @property
    def race(self):
        return self.__race

    @race.setter
    def race(self, race):
        lista = {1: 'Human', 2: 'Elf', 3: 'Dwarf', 4: 'Hobbit', 5: 'Orc'}
        self.__race = lista[race]

    @property
    def hname(self):
        return self.__hname

    @hname.setter
    def hname(self, hname):
        if hname == "Heroe":
            self.__hname = hname + self.nchars
        else:
            self.__hname = hname

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        lista = {1: 'Male', 2: 'Female', 3: 'Other'}
        self.__gender = lista[gender]

    def levelUp(self):
        print("Level Up!!!!!!!!!!!!!!!!!!!!!!!!")
        self.curr_exp -= self.exp
        self.stats_p += 3
        self.exp = self.exp * 2
        self.lv += 1

    def gainExp(self, ex):
        self.curr_exp += ex
        if self.curr_exp >= self.exp:
            self.levelUp()
            self.total_exp += ex

    def death(self):
        self.total_exp -= self.curr_exp * 0.5
        self.curr_exp -= self.curr_exp * 0.5

    def incStats(self, key, n):
        valueKey = self.stats[key]
        valueKey += n
        self.stats[key]= valueKey
        self.stats_p -= n

    def __str__(self):
        string = ""
        for key, value in self.__dict__.items():
            string += key.split("__")[-1] + ": " + str(value) + "\n"
        return string
