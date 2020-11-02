# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:14:00 2020

@author: santhilata
"""


graph1 = {
            'A' : ['B','S'],
            'B' : ['A'],
            'C' : ['D','E','F','S'],
            'D' : ['C'],
            'E' : ['C','H'],
            'F' : ['C','G'],
            'G' : ['F','S'],
            'H' : ['E','G'],
            'S' : ['A','C','G']
            }

def _dfs(graph1, node, visited):
    
    if node not in visited:
        visited.append(node)
        
        for n in graph1[node]:
            _dfs(graph1,n,visited)
            
    return visited

print('dfs')
#visited = _dfs(graph1,'A',[])
#print(visited)

print('******************************')

def _bfs1(node, visited, graph1): 
    
    visited.append(node)
    queue.append(node)
    
    while queue:
        s = queue.pop(0)
        
        print(s, end='->')
        for n in graph1[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
visited= []
queue = []  
print('bfs1')             
#_bfs1('A', visited, graph1)

print('******************************')

    

graph1 = {
    0:[1,2],
    1:[0,2],
    2:[0,1,3],
    3:[3]
    }

def _bfs2(graph1,node): # without recursion , for numeric graphs
    
    visited = [False]*len(graph1)
    queue = []
    queue.append(node)
    visited[node] = True
    
    while queue:
        s = queue.pop(0)
        print(s, end=' ')
        #get all adjacent to s
        for n in graph1[s]:
            if visited[n] == False:
                queue.append(n)
                visited[n] = True
                
    return visited
print('bfs2')
#visited = _bfs2(graph1, 0)
#print(visited)

print('******************************')
graph1 = {
            'A' : ['B','S'],
            'B' : ['A'],
            'C' : ['D','E','F','S'],
            'D' : ['C'],
            'E' : ['C','H'],
            'F' : ['C','G'],
            'G' : ['F','S'],
            'H' : ['E','G'],
            'S' : ['A','C','G']
            }


def dfs_iterating(graph1, node):
    # set is used to mark visited vertices
    visited = set()

    # create a stack for DFS
    stack = []

    # Push vertex s to the stack
    stack.append(node)

    while stack:
        s = stack.pop()
        
        # Stack may contain same vertex twice. So
        # we need to print the popped item only
        # if it is not visited.
        if s not in visited:
            print(s,end =' ')
            visited.add(s)

        # Get all adjacent vertices of current_vertex
        # If an adjacent has not been visited, then push it to stack
        for n in graph1[s]:
            if n not in visited:
                stack.append(n)

print('dfs_iterating')
dfs_iterating(graph1,'A')

print('******************************')
def _bfs1(node,  graph1): 
    visited= set()
    stack = []  
    visited.add(node)
    stack.append(node)
    
    while stack:
        s = stack.pop(0)
        
        print(s, end='->')
        for n in graph1[s]:
            if n not in visited:
                visited.add(n)
                stack.append(n)


print('bfs1')             
_bfs1('A',graph1)

print('******************************')









