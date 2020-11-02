# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:56:04 2020

@author: santhilata

 amazon-interview-questions


Problem:
1. Given a Mix of all types of characters which includes Special characters, Numbers, String in a Log file.
for eg: "HappyI%&&87Christmas %%$^%&NewYear"
2. Get the largest substring which
"contains the Characters in Even Position followed by a Special Character and
then a meaningful word should be coming up"
"""


st = "HappyI%&&87Christmas %%$^%&NewYear"
st = 'happy'

sub_strings = [st[i:i+j] for i in range(len(st)) for j in range(1, len(st)-i+1 )]

## Question is not clear