# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 01:03:52 2017

@author: noname
"""

import json
import model as m

with open('alphabet.json', 'r', encoding='utf-8') as doc:
    alphabet = json.load(doc)

with open('text.txt', 'r', encoding='utf-8') as doc:
    text = doc.read()

x = m.Translator(text, alphabet)
print(x.encode(), end='\n\n')
a = x.decode()
print(a)
