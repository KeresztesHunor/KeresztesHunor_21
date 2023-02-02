# megoldás


def eredmeny(jatekos_lapok: [int], gep_lapok: [int]) -> str:
    jp: int = lapok_osszege(jatekos_lapok)
    gp: int = lapok_osszege(gep_lapok)
    j_db: int = len(jatekos_lapok)
    g_db: int = len(gep_lapok)
    s: str = ""
    if jp <= 21 and gp <= 21:
        if jp > gp:
            s = "J nyert"
        elif gp > jp:
            s = "G nyert"
        elif gp == jp:
            if j_db < g_db:
                s = "J nyert"
            elif g_db > j_db:
                s = "G nyert"
            else:
                s = "döntetlen, osztozok a nyereségen"
    else:
        if jp > 21:
            s = "J vesztett"
        if gp > 21:
            s = "G veszített"
        if jp > 21 and gp > 21:
            s = "döntetlen, a ház nyert"
    return s


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
    vart_eredmeny: str = "J nyert"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("játékos nyert több ponttal teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))


def jatekos_nyert_gep_kifutasaval_teszt():
    jatekos_lapok: [int] = [10, 9, 2]
    gep_lapok: [int] = [10, 9, 3]
    vart_eredmeny: str = "G vesztett"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("játékos nyert a gép kifutásával teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))


def jatekos_nyert_kevesebb_lappal_teszt():
    jatekos_lapok: [int] = [10, 9, 2]
    gep_lapok: [int] = [10, 8, 2, 1]
    vart_eredmeny: str = "J nyert"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("játékos nyert kevesebb lappal teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))


def gep_nyert_tobb_ponttal_teszt():
    jatekos_lapok: [int] = [10, 9, 1]
    gep_lapok: [int] = [10, 9, 2]
    vart_eredmeny: str = "G nyert"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("gép nyert több ponttal teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))


def gep_nyert_jatekos_kifutasaval_teszt():
    jatekos_lapok: [int] = [10, 9, 3]
    gep_lapok: [int] = [10, 9, 2]
    vart_eredmeny: str = "J vesztett"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("gép nyert a játékos kifutásával teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))


def gep_nyert_kevesebb_lappal_teszt():
    jatekos_lapok: [int] = [10, 8, 2, 1]
    gep_lapok: [int] = [10, 9, 2]
    vart_eredmeny: str = "G nyert"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("gép nyert kevesebb lappal teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))


def dontetlen_teszt():
    jatekos_lapok: [int] = [10, 9, 2]
    gep_lapok: [int] = [10, 9, 2]
    vart_eredmeny: str = "döntetlen, osztozok a nyereségen"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("döntetlen teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))


def haz_nyert_teszt():
    jatekos_lapok: [int] = [10, 9, 3]
    gep_lapok: [int] = [10, 9, 3]
    vart_eredmeny: str = "döntetlen, a ház nyert"
    kapott_eredmeny: str = eredmeny(jatekos_lapok, gep_lapok)
    print("ház nyert teszt " + ("sikeres" if vart_eredmeny == kapott_eredmeny else "sikertelen"))
