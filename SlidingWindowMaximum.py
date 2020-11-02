# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:08:05 2020

@author: santhilata
"""
'''
Given an array nums, there is a sliding window of size k which is moving from
 the very left of the array to thevery right. 
 You can only see the k numbers in the window.  
 Each time the sliding window moves right by one position.
'''
import statistics
arr = [1,3,1,2,0,5]
w = 3

def _sliding_window(arr):

    # implement a dequeue
    queue = []
    for i in range(len(arr)):
        
        if len(queue) < 2:
            queue.append(arr[i])
            
            
        else:
            if len(queue) == 3:
                queue.pop(0)
            queue.append(arr[i])
            
            yield statistics.median(queue)
    

queue = _sliding_window(arr)
for i in queue:

    print(i)
    
class MaxHeap:
    
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0 # initially
        self.heap = [0]*(self.maxsize+1)
        self.heap[0] = 9999
        self.front = 1
        
    def parent(self,pos):
        return pos//2
    
    def leftChild(self, pos):
        return 2*pos
    
    def rightChild(self, pos):
        return 2*pos+1
    
    def isLeaf(self, pos):
        if pos >= self.size//2 and pos <= self.size:
            return True
        
        return False
    
    def swap(self, fpos, spos):
        self.heap[fpos],self.heap[spos] = self.heap[spos],self.heap[fpos]
    
#function to heapify the node at a     
    def maxheapify(self, pos):
        
        # if the node is a non leaf and smaller than any child
        # We need to adjust it to its correct position
        
        if not self.isLeaf(pos):
            if self.heap[pos] < self.heap[self.leftChild(pos)] or self.heap[pos] < self.heap[self.rightChild(pos)]:
                
                # swap left or right child and heapify
                
                if self.heap[self.leftChild(pos)] > self.heap[self.rightChild(pos)]:
                    self.swap(pos,self.leftChild(pos))
                    self.maxheapify(self.leftChild(pos))
                    
                else:
                    self.swap(pos,self.rightChild(pos))
                    self.maxheapify(self.rightChild(pos))
                    
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        
        self.size +=1
        self.heap[self.size] = element
        
        current = self.size
        
        while self.heap[current] > self.heap[self.parent(current)]:
            self.swap(current,self.parent(current))
            current = self.parent(current)
        
        
    def Print_heap(self)   :
        for i in range(1,self.size//2+1):
            print('Parent: '+str(self.heap[i]) + ' Left child:'+
                  str(self.heap[2*i]) + ' Right child: '+
                  str(self.heap[2*i+1])
                  )
    def  extractMax(self)      :
        popped = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.maxheapify(self.front)
        return popped
       

if __name__ == "__main__": 
    print('The maxHeap is ') 
    minHeap = MaxHeap(15) 
    minHeap.insert(5) 
    minHeap.insert(3) 
    minHeap.insert(17) 
    minHeap.insert(10) 
    minHeap.insert(84) 
    minHeap.insert(19) 
    minHeap.insert(6) 
    minHeap.insert(22) 
    minHeap.insert(9) 
  
    minHeap.Print_heap() 
    print("The Max val is " + str(minHeap.extractMax()))    
    print("The Max val is " + str(minHeap.extractMax()))     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    