# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:02:47 2020

@author: santhilata

 amazon-interview-questions


A Music app is working on a new feature to pair songs together to play while on the bus. The goal of this feature is to select two songs from a list that will end exactly 30 seconds before the listener reaches their stop. You are tasked with writing the method that selects the songs from a list. Each song is assigned a unique ID, numbered from 0 to N-1.

Assumptions:
1. You will pick exactly two songs.
2. You cannot pick the same song twice.
3. If you have multiple pairs with the same total time, select the pair with the longest song.
4. There are at least two songs available.

Write an algorithm to find the IDs of two songs whose combined runtime will finish exactly 30 seconds before the rider reaches their stop.

Input
The input to the function/method consists of three arguments -
rideDuration, an integer representing the duration of the ride in seconds;
numSongs, an integer representing the number of songs;
songDurations, a list of integers representing the duration of the songs.

Output
Return a pair of integers representing the IDs of two songs whose combined runtime will finish exactly 30 seconds before the rider reaches their stop. If no such pair is possible, return a pair with <-1, -1>.

Constraints
0 ≤ songDurations[i] ≤ 1001
0 ≤ i < numSongs

Example
Input:
rideDuration = 90
numSongs = 5
songDurations = [1, 10, 25, 35, 60]

Output:
[2, 3]

Explanation:
During the ride duration of 90 seconds, the rider listens to the third and fourth songs (2nd and 3rd index, respectively) which end exactly 30 seconds before the bus arrives at their stop.
If two songs have the same duration, select the option with the lowest index.




"""
from itertools import combinations

s = list(map(int, input().rstrip().split()))

ride_duration,num_songs  = s[0], s[1]

song_durations = list(map(int, input().rstrip().split(',')))
 
songs_length = ride_duration - 30
if songs_length < 0:
    print('Journey is too quick')

songs_index = [i for i in range(num_songs)]

two_songs = list(combinations(songs_index,2))

#songs = [songs for songs in two_songs if (song_durations[songs[0]]+song_durations[songs[1]] <= songs_length)]

song_combo = []
for songs in two_songs:
    duration = song_durations[songs[0]]+song_durations[songs[1]]
    if ( duration <= songs_length):
        song_combo.append([duration, songs] )

song_combo1 = sorted(song_combo, reverse = True)

if (len(song_combo1) == 0):
    print(' No two songs present')
    
if (len(song_combo1) >= 1):
    print('songs are', list(song_combo1[0][1]))   


    
    














