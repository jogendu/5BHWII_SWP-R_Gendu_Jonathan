import random
import matplotlib.pyplot as plt


def lottoziehung(List, counter):
    maxN = 44 - counter
    r = random.randrange(0, maxN)

    List[r], List[maxN] = List[maxN], List[r]


def wahrschLotto(lst):
    rand = random.randint(0, 44)
    a = lst[rand] + 1
    lst[rand] = a


if __name__ == '__main__':
    List = list(range(1, 46))

    for counter in range(6):
        lottoziehung(List, counter)
    print("Die Lottozahlen sind:", List[44], List[43], List[42], List[41], List[40], List[39], "\n")

    t = list([0] * 45)
    rang = 1000000
    for x in range(rang):
        wahrschLotto(t)

    plt.bar(range(1, 46), t)
    plt.xlabel('Lottozahlen')
    plt.ylabel('Häufigkeit')
    plt.title('Verteilung der Lottozahlen')
    plt.show()

    # for x in range(45):
    # if t[x] > 0:
    #    perc = t[x]/rang * 100
    # else:
    #    perc = 0
    # print(x+1, "=", t[x],"Mal gezogen   ", str(perc) + "%")
