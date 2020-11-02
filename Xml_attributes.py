# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:47:26 2020

@author: santhilata
"""
'''
6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
'''

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    print(node.attrib)
    return sum(len(elem.attrib) for elem in node.iter())
    

if __name__ == '__main__':
    #n = input()
    xml = input()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))