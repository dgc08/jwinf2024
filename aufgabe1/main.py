#!/usr/bin/env python3

from sys import argv

if __name__ == '__main__':
    if len(argv) < 2:
        users = int(input("Anzahl der Interessenten: "))
        y = int(input("Höhe des Grundstücks"))
        x = int(input("Breite des Grundstücks"))
    else:
        with open(argv[1]) as f:
            users,Y,X = map(int, f.readlines())

    print(users, Y, X)
