"""
Dictionary (wertigkeit der Kombinationen => 1Paar, 2Paare, Straße)
Ohne Objektorientierung(universell) => nur liste(mit 42? zahlen 0-iwas ist 6-ass in der farbe), zuerst wert heraufinden, dann modulo 13 für farbe
Methode mit parameter ob und wieviele z.B.: Paar
"""
import random


def KartenWahrsager(gList):
    karten = []
    for x in gList:
        zahl = (x % 13) + 1
        farbe = x // 13

        karte = [zahl, farbe]
        karten.append(karte)
    return karten


def Zahlenzaehler(hand):
    kartenzaehlerInnen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in hand:
        kartenzaehlerInnen[i[0] - 1] += 1

    while 0 in kartenzaehlerInnen:
        kartenzaehlerInnen.remove(0)

    return kartenzaehlerInnen


def paar(kartenzaehlerInnen):
    if 2 in kartenzaehlerInnen:
        return True
    else:
        return False


def trippling(kartenzaehlerInnen):
    if 3 in kartenzaehlerInnen:
        return True
    else:
        return False


def vierling(kartenzaehlerInnen):
    if 4 in kartenzaehlerInnen:
        return True
    else:
        return False


def zwei_paare(kartenzaehlerIn):
    if 2 in kartenzaehlerIn:
        del kartenzaehlerIn[kartenzaehlerIn.index(2)]
        if 2 in kartenzaehlerIn:
            return True

    else:
        return False


def volles_Haus(kartenzaehlerIn):
    if 2 in kartenzaehlerIn and 3 in kartenzaehlerIn:
        return True

    else:
        return False


def Straße(kartenzaehlerIn):
    kartenzaehlerIn.sort(key=lambda x: x[0])
    if kartenzaehlerIn[0][0] == 1 and kartenzaehlerIn[1][0] == 2 and kartenzaehlerIn[2][0] == 3 and kartenzaehlerIn[3][
        0] == 4 and \
            kartenzaehlerIn[4][0] == 5:
        return True
    for i in range(0, len(kartenzaehlerIn) - 1):
        if kartenzaehlerIn[i][0] != kartenzaehlerIn[i + 1][0] - 1:
            return False
    return True


def spülen(kartenzaehlerin):
    for i in range(0, len(kartenzaehlerin) - 1):
        if kartenzaehlerin[i][1] != kartenzaehlerin[i + 1][1]:
            return False
    return True


def königliche_spülung(kartenzaehlerin):
    kartenzaehlerin.sort(key=lambda x: x[0])
    # check for aces for royal straight flush
    if kartenzaehlerin[0][0] == 1 and kartenzaehlerin[1][0] == 10 and kartenzaehlerin[2][0] == 11 and \
            kartenzaehlerin[3][0] == 12 and \
            kartenzaehlerin[4][0] == 13 and (spülen(kartenzaehlerin) == True):
        return True
    else:
        return False


def strassen_spülung(kartenzaehlerin):
    kartenzaehlerin.sort(key=lambda x: x[0])
    # check for aces for royal straight flush
    if spülen(kartenzaehlerin) and Straße(kartenzaehlerin):
        return True
    else:
        return False


if __name__ == '__main__':
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
            27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
            40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

    gList = []

    for counter in range(5):
        r = random.randrange(0, 51 - counter)
        gList.append(List[r])
        del List[r]

    KartenWahrsager(gList)
