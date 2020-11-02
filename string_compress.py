# -*- coding: utf-8 -*-
"""
Created on Fri May  1 22:07:02 2020

@author: santhilata

 amazon-interview-questions


Here is a question from the "Cracking The Coding Interview" book with a twist.

Implement a method to perform basic string compression using the counts of repeated characters. (p. 73 5th edition)

The twist: the string can also contain digits. Think of encoding and decode protocol.
 How the compression can be reversed properly?

For example, ab2ccccd -> ab24cd
"""

string = 'aaaaabbbb2224cddddd'
str_out = string[0]


i = 1

while (i < len(string)):
    count = 0
    while ((i < len(string)) and (string[i] == string[i-1]))  :
        count = count+1
        i = i+1
        
    if (count >0):
        str_out = str_out[:-1]+str(count+1)+string[i-1]
        
    else:
        str_out = str_out+string[i]
        i = i+1
        
print(str_out)