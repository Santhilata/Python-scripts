# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wd = []
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.wd.append(word)
    def word_equal(self, w1:str, w2:str)->bool:
        
        if len(w1) != len(w2):
            return False
        
        for i in range(len(w1)):
            if w2[i] == '.' :
                continue
            if w1[i]!= w2[i]:
                return False
            
        return True
            
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        l_wd = self.wd
        print(word,l_wd)
        if word in l_wd:
            
            return True
                
        for w in l_wd:
            
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