#!/usr/bin/env python

dict = {}
for l in open("col2.txt"):
	str = l.rstrip()
	if str in dict:
		dict[str] += 1
	else:
		dict[str] = 1

for l in sorted(dict.keys(), key=lambda k:dict[k]):
	print("%s: %d" % (l, dict[l]))