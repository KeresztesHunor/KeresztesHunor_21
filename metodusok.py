# megoldás


def eredmeny(jatekos_lapok: [int], gep_lapok: [int]):
    if lapok_osszege(jatekos_lapok) > 21:
        print("Játékos vesztett")
    if lapok_osszege(gep_lapok) > 21:
        print("Gép vesztett")


def lapok_osszege(lapok: [int]) -> int:
    pontok: int = 0
    for i in range(len(lapok)):
        pontok += lapok[i]
    return pontok


# teszt esetek
