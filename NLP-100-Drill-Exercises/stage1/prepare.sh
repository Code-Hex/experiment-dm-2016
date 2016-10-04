#!/usr/bin/env sh

set -e

wget http://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip
unzip -p ken_all.zip | nkf | python address.py > address.txt
