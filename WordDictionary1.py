#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:12:11 2020

@author: santhilataKV
"""

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wd = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if len(word) in self.wd.keys():
            val = self.wd[len(word)]
            if word not in val:
                self.wd[len(word)].append(word)
        else:
            self.wd[len(word)] = [word]
        
    def word_equal(self, w1:str, w2:str)->bool:
        
        if len(w1) != len(w2):
            return False
        for i in range(len(w1)):
            print(w1,w2)
            if w2[i] == '.' :
                continue
            if w1[i]!= w2[i]:
                return False
            
        return True
            
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        length = len(word)
        if len(self.wd[length]) == 0:
            return False
        if word in self.wd[length]:
            return True
        
        l = self.wd[length]        
        for w in l:
            
            if self.word_equal(w,word):
                
                return True
        return False
obj = WordDictionary()
word = ["bad","dad","mad","pad","bad"]
for w in word:
    obj.addWord(w)
print(obj.wd)
word = ["bad",".ad","b.."]
for w in word:
    param_2 = obj.search(w)
    print(param_2)