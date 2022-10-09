#!/usr/bin/python

import sys

if len(sys.argv) != 3:
    print(f"{sys.argv[0]} inputtext outputlabel")
    quit()

FILENAME = sys.argv[1]
OUTNAME = sys.argv[2]

with open(FILENAME) as f:
    text = f.read() + '\0'

g = open(f'{OUTNAME}.tal', 'w')
g.write(f"@{OUTNAME} ( {FILENAME} )\n")

i = 0
for c in text:
    if i == 0:
        g.write('\t')
    g.write(f"{ord(c):04x}")
    i += 1
    if i < 8:
        g.write(' ')
    else:
        g.write('\n')
        i = 0
