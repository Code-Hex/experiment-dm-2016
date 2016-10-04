#!/usr/bin/env python

for l in open("address.txt"):
	print(l.replace("\t", " "), end="")