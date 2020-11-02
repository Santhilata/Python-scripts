# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:19:30 2020

@author: santhilata
"""

class Class1:
    def m(self):
        print('In class1')
        
class Class2(Class1):
    def m(self):
        print('In class2')
        
class Class3(Class1):
    def m(self):
        print('In class3')
        
class Class4(Class2, Class3):
    pass

obj = Class4()
obj.m()