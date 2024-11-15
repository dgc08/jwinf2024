#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
import math

def q(x,y): # Funktion zur Bestimmung der "Quadratischheit" eines Rechtecks
            # q(x,y) wird größer desto quadratischer die seitenlängen x und y sind, x==y ist "unendlich" quadratisch
    if (x == y):
        return math.inf
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
        y = math.ceil(I/x) # Wenn kein int rauskommt, Aufrunden sodass man knapp über I ist
        
        while q(X/x,Y/y) < q(X/x,Y/(y+1)) and x*y < I*1.1: # solange die "Quadratischheit" größer wird und
            y+=1                                           # man sich unter den 10% befindet, y erhöhen

        if best_q < q(X/x,Y/y): # Falls ein neuer bester Wert gefunden wurde
            best = (x,y)
            best_q = q(X/x,Y/y)

            if "-v" in argv:
                print ("Neue Bestaufteilung: ", x, "*", y, "≙", x*y, "Gärten", f"(Bewertung: {q(X/x, Y/y):.2f})")
        # print(x,y,q(X/x,Y/y))

    if "-v" in argv:
        print("\nErgebnis:", best[0], "*", best[1], "≙", best[0]*best[1], "Gärten")
    else:
        print(argv[1])
        print(best[0])
        print(best[1])
        print(best[0]*best[1])
        print()
