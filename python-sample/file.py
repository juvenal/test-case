#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

# parse text
from parseText import ParseText

print "Informe o arquivo XML para processamento:"
try:
    xmlfile = raw_input('xml file => ')
except EOFError:
    print "Error reading user input"
else:
    print ParseText(xmlfile)
