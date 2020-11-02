# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:09:40 2020

@author: santhilata
"""
'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will 
not be larger than 20,100.

The order of output does not matter.

Example 1:
    Input: s: "cbaebabacd" p: "abc"
    Output : [0,6]
    
Example 2:
    Input: s: "abab" p: "ab"
    Output: [0,1,2]

'''
s= "abab"
p= "ab"
#s= "cbaebabacd" 
#p= "abc"


def _getSignature(st):
    
    arr = [0]*26
    for ch in st:
        pos = ord(ch)-97
        arr[pos] += 1
        
    signature = ''.join([str(i) for i in arr])
    return signature

def _findAnagrams(s, p):
    
    if len(s)<len(p):
        return [-1]
    
    if len(s) == len(p):
        if s==p:
            return [0]
        else:
            return [-1]
    
    window = len(p)
    result =[]
    sign_s = _getSignature(p)
    
    for i in range(len(s)-window+1):
        
        temp = _getSignature(s[i:i+window])
        
        if sign_s == temp:
           
            result.append(i)
        
    return result


result = _findAnagrams(s,p)
print(result)



from collections import Counter

def _findAnagrams1(s,p):
    
    result = []
    if len(s)<len(p):
        return result
    
    if len(s) == len(p):
        if s==p:
            return [0]
        else:
            return result
        
        
    window = len(p)
    
    sign_s = Counter(p)
    
    for i in range(len(s)-window+1):
        
        temp = Counter(s[i:i+window])
        
        if sign_s == temp:
           
            result.append(i)
        
    return result

result = _findAnagrams1(s, p)
print(result)

def findAnagrams_best( s: str, p: str) :
    answer = []
    m, n = len(s), len(p)
    if m < n:
        return answer
    pCounter = Counter(p)
    sCounter = Counter(s[:n-1])
    print(pCounter)
    print(sCounter)

    index = 0
    for index in range(n - 1, m):
            sCounter[s[index]] += 1
            if sCounter == pCounter:
                answer.append(index - n + 1)
            sCounter[s[index - n + 1]] -= 1
            if sCounter[s[index - n + 1]] == 0:
                del sCounter[s[index - n + 1]]
    return answer


result = findAnagrams_best(s, p)
print(result)










