# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:47:27 2020

@author: santhilata
"""
"""
Given a string, determine if it is a palindrome, considering only alphanumeric
 characters and ignoring cases. For example, "Red rum, sir, is murder" 
 is a palindrome, while "Programcreek is awesome" is not.
 Note: Have you consider that the string might be empty? 
 This is a good question to ask during an interview.
 For the purpose of this problem, we define empty string as valid palindrome.
"""

s = "Redrumsirismurder" 
s = s.lower()
t = 'programcreekisawesome' 
t = t.lower()

# palindrome normal

def _palindrome(s):
    
    i = 0
    j = len(s)-1
    
    while i < j:
        
        if s[i] == s[j]:
            i += 1
            j -= 1
            
        else:
            return 'Not palindrome'
        
    return 'palindrome'

#print(_palindrome(s))

def _palin_recur(s):
    
    i = 0
    j = len(s)-1    
    
    if len(s)==0 or len(s) == 1:        
        return True
      
    if s[i] == s[j]:        
        return _palin_recur(s[i+1:j])
        
    else:
        return False
                
print(_palin_recur(s) )       
        
        
        
        
        