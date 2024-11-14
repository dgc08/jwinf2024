#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from math import ceil

def q(x,y): # wird größer desto quadratischer die seitenlängen x und y sind, x==y ist unendlich quadratisch
    if (x == y):
        return float("inf")
    else:
        return abs(1/(1-x/y))

if __name__ == '__main__':
    if len(argv) < 2:
        I = int(input("Anzahl der Interessenten: "))
        Y = int(input("Höhe des Grundstücks: "))
        X = int(input("Breite des Grundstücks: "))
    else:
        with open(argv[1]) as f:
            I,Y,X = map(int, f.readlines())

    if "-v" in argv:
        print("Daten:", I, Y, X)
    best = None
    best_q = 0


    for x in range(1, I+1):
        y = ceil(I/x) #
        while q(X/x,Y/y) < q(X/x,Y/(y+1)) and x*y < I*1.1:
            y+=1

        if best_q < q(X/x,Y/y):
            best = (x,y)
            best_q = q(X/x,Y/y)

            if "-v" in argv:
                print ("Neue beste Aufteilung gefunden: ", x, "*", y, "a", x*y, "Gärten")
        # print(x,y,q(X/x,Y/y))

    if "-v" in argv:
        print("\nErgebnis:", best[0], "*", best[1], "a", best[0]*best[1], "Gärten")
    else:
        print(best[0])
        print(best[1])
        print(best[0]*best[0])
