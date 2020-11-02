# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:43:46 2020

@author: santhilata

abstraction in python
"""

'''
from abc import ABC, abstractmethod
class Polygon(ABC):
    
    # abstract method
    def noofsides(self):
        pass
    
class Hexagon(Polygon):
    
    def __init__(self):
        self.sides = 6
    
    #override abstract method
    def noofsides(self):
        return self.sides

hex = Hexagon()
print('hex is ; ', hex.noofsides())


import abc

class parent:
    def geeks(self):
        return 55
    
class child(parent):
    def geeks(self):
        print('child class')
        
c = child()

p = parent()
print(p.geeks())


# Python program invoking a  
# method using super() 
  
import abc 
from abc import ABC, abstractmethod 
  
class R(ABC): 
    def rk(self): 
        print("Abstract Base Class") 
  
class K(R): 
    def rk(self): 
        super().rk() 
        print("subclass ") 
  
# Driver code 
r = K() 
r.rk() 


# Python program showing 
# abstract properties 
  
import abc 
from abc import ABC, abstractmethod 
  
class parent(ABC): 
    @abc.abstractproperty 
    def geeks(self): 
        return "parent class"
class child(parent): 
       
    @property
    def geeks(self): 
        return "child class"
   
   
try: 
    r =parent() 
    print( r.geeks) 
except Exception as err: 
    print (err) 
   
r = child() 
print (r.geeks) 

'''

# Python program showing 
# abstract class cannot 
# be an instantiation 
from abc import ABC,abstractmethod 
  
class Animal(ABC): 
    @abstractmethod
    def move(self): 
        pass
class Human(Animal): 
    def move(self): 
        print("I can walk and run") 
  
class Snake(Animal): 
    def move(self): 
        print("I can crawl") 
  
class Dog(Animal): 
    def move(self): 
        print("I can bark") 
  
class Lion(Animal): 
    def move(self): 
        print("I can roar") 
  
c=Animal() 
#c = Human()
c.move()


