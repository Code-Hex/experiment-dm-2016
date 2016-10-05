#!/usr/bin/env python

import sys
import os

argv = sys.argv
N = int(argv[1])

lines = list(open("address.txt"))
for line in lines[len(lines) - N:]:
	print(line, end="")