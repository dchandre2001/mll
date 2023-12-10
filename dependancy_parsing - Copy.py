# -*- coding: utf-8 -*-
"""Dependancy parsing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1INcXfezaQAkWH36BIhOpREn5O97-Xo6H
"""

import spacy
from spacy import displacy
nlp=spacy.load("en_core_web_sm")
text="I am Dipali from Nashik."
about_text=nlp(text)
for token in about_text:
  print(f"""
      TOKEN:{token.text}
      {token.tag_=}
      {token.head.text=}
      {token.dep_=}""")

displacy.render(about_text,style="dep",jupyter=True)