#!/usr/bin/env python

print(sorted([l.split("\t") for l in open("address.txt")], key=lambda v:v[1]))