

from champion import Champion



if __name__ == "__main__":



    race = 1
    gender = 2

    p2 = Champion(1, "one", race, 1)
    p2.create()

    print(p2)


    p3 = Champion(2, "two", race, gender)
    print(p3)
    p2.gainExp(130)
    print(p2)
    p2.death()
    print(p2)

    p2.incStats('Defense', 2)
    p2.incStats('Magic', 1)

    print(p2)