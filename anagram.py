#!/usr/bin/python
import fileinput
for line in fileinput.input():
        words = line.split()
sortedword ={}
for word in words:
    key = "".join(sorted(word.lower()))
    if not sortedword.has_key(key):
        sortedword[key] = []
    sortedword[key].append(word)
for key in sortedword:
   print sortedword[key]
