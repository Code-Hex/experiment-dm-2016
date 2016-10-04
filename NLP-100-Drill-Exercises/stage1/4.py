#!/usr/bin/env python

with open("col1.txt") as col1, open("col2.txt") as col2:
	for c1, c2 in zip(col1, col2):
		print("{0}\t{1}".format(c1.strip(), c2.strip()))