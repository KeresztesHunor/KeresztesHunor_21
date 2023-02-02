# megoldás


def eredmeny(jatekos_lapok: [int], gep_lapok: [int]) -> str:
    jatekos_pont: int = lapok_osszege(jatekos_lapok)
    gep_pont: int = lapok_osszege(gep_lapok)
    if jatekos_pont > 21 and gep_pont > 21:
        return "Ház nyert"
    elif jatekos_pont > 21:
        return "Játékos vesztett"
    else:
        return "Gép vesztett"


def lapok_osszege(lapok: [int]) -> int:
    pontok: int = 0
    for i in range(len(lapok)):
        pontok += lapok[i]
    return pontok


# teszt esetek


def jatekos_nyert_teszt():
    print("sikeres" if eredmeny([10, 9, 2], [10, 9, 3]) == "Gép vesztett" else "sikertelen")
