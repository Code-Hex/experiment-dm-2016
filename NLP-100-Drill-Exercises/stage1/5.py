#!/usr/bin/env python

import sys

argv = sys.argv
N = int(argv[1])
i = 0
for l in open("address.txt"):
	i += 1
	print(l, end="")
	if i == N: break
