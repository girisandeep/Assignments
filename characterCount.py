#!/usr/bin/python
import fileinput
for line in fileinput.input():
        List = list(line)
        Uniq = set(List)
for key in Uniq:
        print (key, line.count(key))