#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python

def numsum(no1):
    results = 0
    while no1 > 0:
        remainder = no1 % 10
        results += (remainder)**3
        no1 = (no1-remainder)/10
    return results
    
 


