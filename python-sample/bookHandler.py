#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import xml.sax.handler

class BookHandler(xml.sax.handler.ContentHandler):
	def __init__(self):
		self.buffer = ""

	def startElement(self, name, attributes):
		print "Abrindo elemento " + name
		if attributes.getLength() > 0:
			print "com atributos "
			for attr in attributes.getNames():
				print attr

	def characters(self, data):
		if data == '\n':
			self.buffer += "<br>"
		self.buffer += data

	def endElement(self, name):
		print "Fechando elemento " + name

