#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.lista = []
        self.etiqueta = {"root-layout", "region", "img", "audio", "textstream"}
        self.atributo = {
            "root-layout": ["width", "height", "background-color"],
            "region": ["id", "top", "bottom", "left", "right"],
            "img": ["src", "region", "begin", "dur"],
            "audio": ["src", "begin", "dur"],
            "textstream": ["src", "region"]
            }

    def startElement(self, name, attrs):
        if name in self.etiqueta:
            Dic = {}
            Dic['etiqueta'] = name
            
            for Atributo in self.atributo[name]:
                Dic[Atributo] = attrs.get(Atributo, "")
            self.lista.append(Dic)

    def get_tags(self):
        return self.lista

if __name__ == "__main__":
    """
    main program
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    
    lista = cHandler.get_tags()
    print (lista)
