#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv

alph = 'abcdefghijklmnopqrstuvwxyzäöüß'

def process_text(text):
    text = text.lower().strip()

    ret_text = ""

    for char in text:
        if char in alph:
            ret_text += char

    return ret_text

def numberify(text):
    ret = []
    for char in text:
        ret.append(alph.index(char)+1) # Man fängt bei 0 an zu zählen, 'a' soll aber 1 sein

    return ret

def get_winner(numbers):
    nlen = len(numbers)
    if nlen < 2:
        print("Text ist zu klein, nicht jeder hat ein Startpunkt.")
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

    with open(argv[1]) as f:
        text = process_text(f.read())
    #print(text)

    numbers = numberify(text)
    #print(numbers)

    print("Der Gewinner ist Spieler", get_winner(numbers))
