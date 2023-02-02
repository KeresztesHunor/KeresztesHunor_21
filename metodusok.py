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


def jatekos_nyert_tobb_ponttal_teszt():
    jatekos_lapok: [int] = [10, 9, 2]
    gep_lapok: [int] = [10, 9, 1]
    vart_eredmeny: str = "Gép vesztett"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("játékos nyert teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))


def jatekos_nyert_gep_kifutasaval_teszt():
    jatekos_lapok: [int] = [10, 9, 2]
    gep_lapok: [int] = [10, 9, 3]
    vart_eredmeny: str = "Gép vesztett"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("játékos nyert teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))


def jatekos_nyert_kevesebb_lappal_teszt():
    jatekos_lapok: [int] = [10, 9, 2]
    gep_lapok: [int] = [10, 8, 2, 1]
    vart_eredmeny: str = "Gép vesztett"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("játékos nyert teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))
