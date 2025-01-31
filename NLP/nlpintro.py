# -*- coding: utf-8 -*-
"""
Created on Sat May 23 13:53:18 2020

@author: caleb
"""

import spacy
from spacy.matcher import PhraseMatcher


nlp = spacy.load('en_core_web_sm')

doc = nlp("Tea is healthy and calming, don't you think?")
'''
for token in doc:
    print(token)
    
print(f"Token \t\tLemma \t\tStopword".format('Token', 'Lemma', 'Stopword'))
print("-"*40)
for token in doc:
    print(f"{str(token)}\t\t{token.lemma_}\t\t{token.is_stop}")
'''    
matcher = PhraseMatcher(nlp.vocab, attr='LOWER')

terms = ['Galaxy Note', 'iPhone 11', 'iPhone XS', 'Google Pixel']
patterns = [nlp(text) for text in terms]
matcher.add("TerminologyList", None, *patterns)

text_doc = nlp("Glowing review overall, and some really interesting side-by-side "
               "photography tests pitting the iPhone 11 Pro against the "
               "Galaxy Note 10 Plus and last year’s iPhone XS and Google Pixel 3.") 
matches = matcher(text_doc)

match_id, start, end = matches[3]
print(nlp.vocab.strings[match_id], text_doc[start:end])