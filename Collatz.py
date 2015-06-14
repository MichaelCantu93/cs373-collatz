#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

global cache
cache = {}

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert type(i) is int
    assert type(j) is int
    
    assert i >=1 and i <= 999999
    assert j >=1 and j <= 999999

    if i > j:
        temp = 0
        temp = i
        i = j
        j = temp

    assert i <= j
   
    index = 0
    maxCount = 0 
    count = 1   
     
    for x in range(i, j+1):
        index = x
        while x > 1:
            if str(x) in cache:
                count = count + cache[str(x)] - 1
                x = 1
            else:
                if x%2 == 0:
                    x = x >> 1
                    count += 1
                else:
                    x = x + (x >> 1) + 1
                    count += 2
                    
        if not str(index) in cache:
            cache[str(index)] = count
            
        if count >= maxCount:
            maxCount = count
            count = 1
        else:
            count = 1
            
    assert maxCount >= count
    assert maxCount > 0

    return maxCount

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
