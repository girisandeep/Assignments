#!/usr/bin/python
import fileinput
DNA ={}
for line in fileinput.input():
    invertedStr = " ".join(line.split()[::-1])
    words = invertedStr.split()
    key = words[0]
    if not DNA.has_key(key):
        DNA[key] = []
    DNA[key].append(words[1])
for key in DNA:
    print DNA[key]