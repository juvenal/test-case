#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import xml.sax

from bookHandler import BookHandler

def ParseText(XMLfilename):
	parser = xml.sax.make_parser()
	handler = BookHandler()
	parser.setContentHandler(handler)
	parser.parse(XMLfilename)
	return handler.buffer

