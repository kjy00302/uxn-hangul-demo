#!/usr/bin/python

import sys

if len(sys.argv) != 3:
    print(f"{sys.argv[0]} inputfont outputlabel")
    quit()

FONTNAME = sys.argv[1]
OUTNAME = sys.argv[2]

"""
Needs to convert one 16*16 tile into four 8*8 tiles

TILE ORDER
1 3

2 4

"""

with open(FONTNAME, 'rb') as f:
    g = open(f'{OUTNAME}.tal', 'w')
    g.write(f"@{OUTNAME} ( {FONTNAME} )\n")
    while f.peek(1) != b'':
        g.write("\t")
        a = bytearray()
        b = bytearray()
        c = []
        for i in range(16):
            a += f.read(1)
            b += f.read(1)
        c.extend(( a[i*2:i*2+2].hex() for i in range(8)))
        c.extend(( b[i*2:i*2+2].hex() for i in range(8)))
        g.write(" ".join(c))
            
        g.write("\n")
