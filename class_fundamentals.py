# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:10:55 2020

@author: santhilata


Python class fundamentals
"""

class Base:
    def __init__(self):
        # protected member
        self.a = 2
        self.__c = 'c'
    def print_c(self):
        return self.__c

#creating a derived class        
class Derived(Base):
    def __init__(self):
        
        # calling constructor of the base class
        Base.__init__(self)
        print('calling private member;', self.__a)
        
obj1 = Base()
#print(obj1.a)
#print(obj1.c) # raises error as it is private member
#print(obj1.print_c())
obj2 = Derived()

