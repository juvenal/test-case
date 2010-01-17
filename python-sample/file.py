#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import codecs

# variáveis
text_name = "exemplo"

#f = open(text_name+".html",'w+')
f = codecs.open(text_name + ".html", 'w+', 'iso-8859-1')

# parse text
from parseText import ParseText

print "Informe o arquivo XML para processamento: "

texto = ParseText('pagina.xml')
f.write(texto+'\n')

# script identifier
f.write(u"<!-- Página gerada automaticamente por um script python\n\
written in Eclipse-Pydev -->\n")
f.close()
