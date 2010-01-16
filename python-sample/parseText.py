#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import xml.sax
import xml.sax.handler
import pprint

class BookHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.buffer = ""

    def characters(self, data):
        if data == '\n':
            self.buffer += "<br>"
        self.buffer += data


def ParseText(XMLfilename):
    parser = xml.sax.make_parser()
    handler = BookHandler()
    parser.setContentHandler(handler)
    parser.parse(XMLfilename)
    return handler.buffer

