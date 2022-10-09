#!/usr/bin/python

import sys

if len(sys.argv) != 3:
    print(f"{sys.argv[0]} inputfile outputlabel")
    quit()


FILENAME = sys.argv[1]
OUTNAME = sys.argv[2]

with open(FILENAME, 'rb') as f:
    g = open(f'{OUTNAME}.tal', 'w')
    g.write(f"@{OUTNAME} ( {FILENAME} )\n")
    
    while f.peek(1) != b'':
        g.write("\t")
        g.write(" ".join((f.read(2).hex() for i in range(8))).rstrip())
        g.write("\n")
