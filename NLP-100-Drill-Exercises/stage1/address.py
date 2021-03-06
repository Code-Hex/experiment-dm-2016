#!/usr/bin/env python

import sys
import csv

D = set()
for row in csv.reader(sys.stdin):
    s1 = ''.join((row[6], row[7]))
    s2 = row[8]
    if s2 == '以下に掲載がない場合':
        continue
    s = s2.split('、')[0]
    p = s.find('（')
    if p != -1:
        s = s[:p]
    D.add((s1, s))

for s1, s2 in D:
    print('\t'.join((s1, s2)))
