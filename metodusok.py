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


def teszt_esetek():
    jatekos_nyert_tobb_ponttal_teszt()
    jatekos_nyert_gep_kifutasaval_teszt()
    jatekos_nyert_kevesebb_lappal_teszt()
    gep_nyert_tobb_ponttal_teszt()
    gep_nyert_jatekos_kifutasaval_teszt()
    gep_nyert_kevesebb_lappal_teszt()
    dontetlen_teszt()
    haz_nyert_teszt()


def jatekos_nyert_tobb_ponttal_teszt():
    jatekos_lapok: [int] = [10, 9, 2]
    gep_lapok: [int] = [10, 9, 1]
    vart_eredmeny: str = "Gép vesztett"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("játékos nyert több ponttal teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))


def jatekos_nyert_gep_kifutasaval_teszt():
    jatekos_lapok: [int] = [10, 9, 2]
    gep_lapok: [int] = [10, 9, 3]
    vart_eredmeny: str = "Gép vesztett"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("játékos nyert a gép kifutásával teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))


def jatekos_nyert_kevesebb_lappal_teszt():
    jatekos_lapok: [int] = [10, 9, 2]
    gep_lapok: [int] = [10, 8, 2, 1]
    vart_eredmeny: str = "Gép vesztett"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("játékos nyert kevesebb lappal teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))


def gep_nyert_tobb_ponttal_teszt():
    jatekos_lapok: [int] = [10, 9, 1]
    gep_lapok: [int] = [10, 9, 2]
    vart_eredmeny: str = "Játékos vesztett"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("gép nyert több ponttal teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))


def gep_nyert_jatekos_kifutasaval_teszt():
    jatekos_lapok: [int] = [10, 9, 3]
    gep_lapok: [int] = [10, 9, 2]
    vart_eredmeny: str = "Játékos vesztett"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("gép nyert a gép kifutásával teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))


def gep_nyert_kevesebb_lappal_teszt():
    jatekos_lapok: [int] = [10, 8, 2, 1]
    gep_lapok: [int] = [10, 9, 2]
    vart_eredmeny: str = "Játékos vesztett"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("gép nyert kevesebb lappal teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))


def dontetlen_teszt():
    jatekos_lapok: [int] = [10, 9, 2]
    gep_lapok: [int] = [10, 9, 2]
    vart_eredmeny: str = "Döntetlen"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("döntetlen teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))


def haz_nyert_teszt():
    jatekos_lapok: [int] = [10, 9, 3]
    gep_lapok: [int] = [10, 9, 3]
    vart_eredmeny: str = "Ház nyert"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("ház nyert teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))
