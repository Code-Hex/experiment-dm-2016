#!/usr/bin/env python

import os

col1 = open("col1.txt", "w")
col2 = open("col2.txt", "w")

for l in open("address.txt"):
	line = l.split("\t")

	col1.write(line[0] + "\n")
	col2.write(line[1])

pos = col1.tell() - 1
col1.seek(pos, os.SEEK_SET)
col2.seek(pos, os.SEEK_SET)

col1.truncate()
col2.truncate()

