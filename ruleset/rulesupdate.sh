#!/bin/sh
CLIENT_ID=${CLIENT_ID}
CLIENT_SECRET=${CLIENT_SECRET}

cd /usr/share/python

mkdir suricata

python3 rulesw.py

tar zxf scw.tgz -C /usr/share/python/suricata

chown ????:????? /usr/share/python/suricata




