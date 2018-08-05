# -*- coding: utf-8 -*-

from sys import argv


script, filename = argv

txt = open(filename)

print "the filename : %s " % filename
print txt.read()


print "input the filename again"
file_a = raw_input("> ")

txt_a = open(file_a)
print txt_a.read()

