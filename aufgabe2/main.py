#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv

alph = 'abcdefghijklmnopqrstuvwxyzäöüß'

def process_text(text):
    text = text.lower().strip()

    ret = []

    for char in text:
        if char in alph:
            ret.append(alph.index(char)+1) # Man fängt bei 0 an zu zählen, 'a' soll aber 1 sein
        #else: # wird geskippt

    return ret

def get_winner(numbers):
    nlen = len(numbers)
    if nlen < 2:
        print("Text ist zu klein, nicht jeder hat ein Startpunkt.")
        exit(1)
    a = 0
    b = 1

    a_won = False
    b_won = False

    while (not a_won) and (not b_won):
        a += numbers[a]
        b += numbers[b]

        if a >= nlen:
            a_won = True
            break
        if b >= nlen:
            b_won = True
        
    winner = 1
    if b_won:
        winner = 2

    return winner

if __name__ == '__main__':
    if len(argv) < 2:
        print("Gebe den Dateinamen des zu testenden Textes an")
        exit(1)

    with open(argv[1]) as f:
        numbers = process_text(f.read())

    print(argv[1])
    print("Spieler", get_winner(numbers), "gewinnt")
    print()
