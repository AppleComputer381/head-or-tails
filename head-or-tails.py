import random
import matplotlib.pyplot as plt
import numpy as np
import pylab


def hasard(n):

    assert n > 15, "Vous ne pouvez pas utiliser cette fonction avec un nombre inferieur a 15"
    pile = 0
    face = 0
    for i in range(n):
        choix = random.choice(["pile", "face"])
        if choix == "pile":
            pile = pile + 1

        else:
            face= face+1

    fig = plt.figure()

    x = [1, 2]
    height = []
    height.append(pile)
    height.append(face)
    width = 0.05
    BarName = ['pile','face']

    plt.bar(x, height, width, color=(0.65098041296005249, 0.80784314870834351, 0.89019608497619629, 1.0) )
    plt.scatter([i+width/2.0 for i in x],height,color='k',s=40)

    plt.xlim(0,11)
    plt.ylim(0,n/1,75)
    plt.grid()

    plt.ylabel('Fréquences')
    plt.title('Statistiques sur la fréquences de la sortie de pile et face')

    pylab.xticks(x, BarName, rotation=40)

    plt.savefig('SimpleBar.png')
    plt.show()

def comptage(n):

    c=0

    while n>0 :
        c= c +1
        print(c)
        n= n-1
