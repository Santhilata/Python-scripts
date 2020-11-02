# -*- coding: utf-8 -*-
"""
Created on Fri May  1 06:48:56 2020

@author: santhilata

 amazon-interview-questions
0
of 0 votes
3
Answers

You are given 2 arrays: one representing the time people arrive at a door
 and other representing the direction they want to go(in or out) You have to find
 at what time each person will use the door provided no 2 people can use the door
 at the same time. Constraints: the door starts with ‘in’ position, in case of a
 conflict(2 or more people trying to use the door at the same time), the direction
 previously used holds precedence. If there is no conflict whoever comes first uses
 the door. Also if no one uses the door, 
it reverts back to the starting ‘in’ position. Should be linear time complexity.
"""


from collections import defaultdict

data = input().split('\n')

arrival_time = list(map(int,data[0].rstrip().split()))
in_out = list(data[1].rstrip().split())

input_dict = defaultdict(list)
for k,v in sorted(zip(arrival_time,in_out)):
    input_dict[k].append(v)
 


direction = 'in'

visitor = []
for k, v in input_dict.items():
    flag = 1
    for i in v:
        if i == direction:
            visitor.append((k,i))
            
        
    for i in v:
        
        if i != direction:
            flag = 0
            visitor.append((k,i))
            
    if flag ==0:
        direction = 'out' if direction =='in' else 'out'

print(visitor)
                 

     



      
    