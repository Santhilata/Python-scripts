# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:05:19 2020

@author: santhilata

implement BFS in python
"""


graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = []
queue = []

def BFS(start, visited, graph):
    
    visited.append(start)
    queue.append(start)
    
    while len(queue) >0:
        s = queue.pop(0)
        print( 'nodes:', s)
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
                
BFS('A', visited, graph)