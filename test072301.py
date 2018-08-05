# -*- coding:utf-8 -*-

from sys import exit

def gold_room():
    print "This room is full of gold. How much do U take?"
    
    how_much = 0
    next = raw_input(">")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Men, learn to type a number.")
    if how_much < 50:
        print "Nice, you're not greedy, winwin!"
        exit(0)
    else:
        dead("You greedy bastard!")

#死亡说明
def dead(why = "Game over!"):
    print why, "Good job!"

gold_room()