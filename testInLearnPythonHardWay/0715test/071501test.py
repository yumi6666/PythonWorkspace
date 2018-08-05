# -*-coding: utf-8 -*-

from sys import argv

script , filename = argv

print "try to erase %r" % filename

raw_input('?')

print "opening the file.."

target = open(filename,'w')

print "Truncating the file?"
target.truncate()

print"Now write some words in it."
line1 = raw_input("line1:")
line2 = raw_input("line2:")

target.write(line1)
target.write(line2)

print"And we finally close it."
target.close()