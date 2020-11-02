# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 07:27:18 2020

@author: sa'nthilata
"""


class Solution:
    """
    def _isPalindrome(self, s:str) -> bool:
        
        if len(s) == 0:
            return True
        
        if len(s) == 1:
            return True
        
        if (s[0] == s[-1]):
            
            return self._isPalindrome(s[1:-1])
        
        else:
            return False
        
    def longestPalindrome(self, s: str) -> str:
        
        palins = set()
        
        for i in range(len(s)):
            
            for j in range(i, len(s)):
                #print(s[i:j+1])
                if (self._isPalindrome(s[i:j+1])):
                    
                    palins.add(s[i:j+1])
                    
        max_len = 0
        max_palin = ''
        for st in palins:
            if len(st) > max_len:
                max_len = len(st)
                max_palin = st
                
        return max_palin
    """
    
    def _isPalindrome(self, s:str) -> bool:
        
        if len(s) == 0:
            return True
        
        if len(s) == 1:
            return True
        
        if (s[0] == s[-1]):
            return self._isPalindrome(s[1:-1])
        
        else:
            return False
        
    def longestPalindrome(self, s: str) -> str:        
        #palins = set()
        max_len = 0
        max_palin = ''
        
        for i in range(len(s)):
            
            for j in range(i, len(s)):
                
                if (j+1-i >= max_len) :
                    if (self._isPalindrome(s[i:j+1])):
                        max_len = len(s[i:j+1])
                        max_palin = s[i:j+1]
                                        
                else:
                    break      
                
        return max_palin
    
sol = Solution()    

s = 'babad'
s = 'a'
s = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"

s = 'cbbd'
ans = sol.longestPalindrome(s)
print(ans)