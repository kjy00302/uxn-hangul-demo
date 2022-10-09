#!/usr/bin/python

import sys

if len(sys.argv) != 3:
    print(f"{sys.argv[0]} inputfont outputlabel")
    quit()

FONTNAME = sys.argv[1]
OUTNAME = sys.argv[2]

# Only include 96 character
TRUNCATE = True

with open(FONTNAME, 'rb') as f:
    g = open(f'{OUTNAME}.tal', 'w')
    g.write(f"@{OUTNAME} ( {FONTNAME} )\n")
    
    if TRUNCATE:
        f.seek(32)
        for i in range(6): # 96 / 16 = 6
            g.write("\t")
            g.write(" ".join(( f.read(2).hex() for i in range(8))))
            g.write("\n")
    else:
        for i in range(16): # 256 / 16 = 16
            g.write("\t")
            g.write(" ".join(( f.read(2).hex() for i in range(8))))
            g.write("\n")
    
    g.write("\t&glyphs\n")
    if TRUNCATE:
        f.seek(1280)
        for i in range(192): # 3072 / 16 = 192
            g.write("\t")
            g.write(" ".join(( f.read(2).hex() for i in range(8))))
            g.write("\n")
    else:
        for i in range(1024): # 8192 / 16 = 1024
            g.write("\t")
            g.write(" ".join(( f.read(2).hex() for i in range(8))))
            g.write("\n")
