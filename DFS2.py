# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 09:51:22 2020

@author: santhilata
"""

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFS(self,v,vertex):
        visited = [False]*vertex
        print(self. graph)
        # print(len(self.graph),"+++")
        self.DFSUtil(v,visited)

    def DFSUtil(self,v,visited):
        visited[v]=True
        print(v)

        for i in self.graph[v]:
            if visited[i] == False:
                # print(visited)
                self.DFSUtil(i,visited)
g= Graph()

vertex=7

g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,6)
g.addEdge(0,5)
g.addEdge(5,3)
g.addEdge(5,4)
g.addEdge(4,3)
g.addEdge(6,4)

g.DFS(0,vertex)