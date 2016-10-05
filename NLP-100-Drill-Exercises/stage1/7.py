#!/usr/bin/env python

dict = {}

for line in open("address.txt"):
	col = line.split("\t")
	dict[col[0]] = True

print(len(dict.keys()))