#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
import math

def q(x,y): # Funktion zur Bestimmung der "Quadratischheit" eines Rechtecks
            # q(x,y) wird kleiner desto quadratischer die seitenlängen x und y sind, für x==y ist q(x,y) = 0
    return abs(1-x/y)

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
    best_q = math.inf # am anfang gibt es keine beste konfiguration

    for x in range(1, I+1):
        y = math.ceil(I/x) # Wenn kein int rauskommt, Aufrunden sodass man knapp über x ist
        
        while q(X/x,Y/(y+1)) < q(X/x,Y/y) and x*y < I*1.1: # solange q(x,y) kleiner wird,
                                                           # das heißt das Rechteck quadratischer wird und
            y+=1                                           # man sich unter den 10% befindet, y erhöhen

        # print(x,y,q(X/x,Y/y))
        if q(X/x,Y/y) < best_q : # Falls ein neuer bester Wert gefunden wurde
            best = (x,y)
            best_q = q(X/x,Y/y)

            if "-v" in argv:
                print ("Neue Bestaufteilung: ", x, "*", y, "≙", x*y, "Gärten", f"(Bewertung: {q(X/x, Y/y):.2f})")

    if "-v" in argv:
        print("\nErgebnis:", best[0], "*", best[1], "≙", best[0]*best[1], "Gärten")
    else:
        print(argv[1])
        print(best[0])
        print(best[1])
        print(best[0]*best[1])
        print()
