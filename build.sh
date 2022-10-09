#!/bin/sh

./utils/844conv.py assets/H01.HAN font-844
mv font-844.tal assets-build/.

./utils/uf2conv.py assets/sans14-regular.uf2 font-uf2
mv font-uf2.tal assets-build/.

./utils/textencoder.py assets/text.txt text
mv text.tal assets-build/.

./utils/talconv.py assets/sejong1ex1e.icn sejong
mv sejong.tal assets-build/.

uxnasm src/main.tal demo.rom
