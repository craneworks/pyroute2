#!/usr/bin/python
'''
Usage::

    ./decoder.py [module] [data_file]

Sample::

    ./decoder.py tcmsg ./sample_packet_01.data

Module is a name within rtnl hierarchy. File should be a
binary data in the escaped string format (see samples).
'''
import io
import sys
from pprint import pprint
from importlib import import_module

template = 'pyroute2.netlink.rtnl.{mod}.{mod}'
mod = sys.argv[1]
f = open(sys.argv[2], 'r')
b = io.BytesIO()
s = template.format(mod=mod).split('.')
package = '.'.join(s[:-1])
module = s[-1]
m = import_module(package)
met = getattr(m, module)


for a in f.readlines():
    if a[0] == '#':
        continue
    while True:
        try:
            b.write(chr(int(a[2:4], 16)))
        except:
            break
        a = a[4:]

b.seek(0)
t = met(b)
t.decode()
pprint(t)
