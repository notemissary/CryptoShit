# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 00:42:06 2017

@author: noname
"""


class Translator:
    """Translator class

    This class can encode a text written in russian to same keys but with
    english layout. Decoding does the reverse thing

    param:
        text - a string to operate
        alphabet - a dictionary for encoding or decoding text
    """
    __alphabet = {}

    def __init__(self, text, alphabet):
        self.__alphabet.update(alphabet)
        self.__text = text.lower()

    def decode(self):
        self.__output = ''
        for i in self.__text:
            if i in self.__alphabet.keys():
                self.__output += self.__alphabet[i]
            else:
                self.__output += i
        return self.__output

    def encode(self):
        self.__output = ''
        for i in self.__text:
            for k in self.__alphabet.keys():
                if self.__alphabet[k] == i:
                    self.__output += k
                    break
            else:
                self.__output += i
        return self.__output
