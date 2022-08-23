#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str.split().pop(5) + " " + str.split().pop(6) + " " + str.split().pop(-4) + " " + str.split().pop(0)
print(str)
