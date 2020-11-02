# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:31:20 2020

@author: santhilata

 amazon-interview-questions


A 2d array has 0 and 1 as values. In one flip, 0's are changed to 1 if and only if
any of the neighbors (left, right, top, bottom) is 1. Return the total number of flips
required to convert the whole grid to 1's


"""


def get_neighbours(row, col):
    if row == 0:
        return [(row)


file = open("data.txt", "r")          # open file for reading

var = [[int(n) for n in line.strip().split(' ')] for line in file]
                                      # thus creating an array of arrays.
file.close()                          # close file.

print(len(var))

flag = True

rows = len(var)
cols = len(var[0])


        
    