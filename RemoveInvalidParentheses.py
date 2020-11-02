# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:17:31 2020

@author: santhilata
"""

'''
Remove the minimum number of invalid parentheses in order to make the input string valid.
 Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Input: "()())()"
Output: ["()()()", "(())()"]

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Input: ")("
Output: [""]
'''

#use of stacks

def isParenthesis(c): 
    return ((c == '(') or (c == ')'))  
  
# method returns true if contains valid  
# parenthesis  
def isValidString(str): 
    cnt = 0
    for i in range(len(str)): 
        if (str[i] == '('): 
            cnt += 1
        elif (str[i] == ')'): 
            cnt -= 1
        if (cnt < 0): 
            return False
    return (cnt == 0) 

# method to remove invalid parenthesis  
def removeInvalidParenthesis(st): 
    if (len(st) == 0): 
        return
          
    # visit set to ignore already visited  
    visit = set() 
      
    # queue to maintain BFS 
    q = [] 
    temp = 0
    level = 0
      
    # pushing given as starting node into queu 
    q.append(st) 
    visit.add(st) 
    
    
    while(len(q)): 
        st =   q.pop()  #q[0] 
        
       
        if (isValidString(st)): 
            print(st) 
              
            # If answer is found, make level true  
            # so that valid of only that level  
            # are processed.  
            level = True
        if (level): 
            continue
        for i in range(len(st)): 
            if (not isParenthesis(st[i])): 
                continue
                  
            # Removing parenthesis from str and  
            # pushing into queue,if not visited already  
            temp = st[0:i] + st[i + 1:]  
            if temp not in visit: 
                q.append(temp) 
                visit.add(temp) 
                

expression = "()())()"
removeInvalidParenthesis(expression) 
expression = "()v)"
removeInvalidParenthesis(expression)                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                