# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:57:19 2020

@author: santhilata
"""

from collections import Counter
from itertools import combinations

def sherlockAndAnagrams(s):
    n = len(s)
    res = 0
    for l in range(1, n):
        cnt = {}
        for i in range(n - l + 1):
            subs = list(s[i:i + l])
            subs.sort()
            subs = ''.join(subs)
            if subs in cnt:
                cnt[subs] += 1
                print(subs)
            else:
                cnt[subs] = 1
            res += cnt[subs] - 1
    return(res)

if __name__ == '__main__':
    

    q = int(input())

    for q_itr in range(q):
        s = input()
        
        result = sherlockAndAnagrams(s)

        print(result)