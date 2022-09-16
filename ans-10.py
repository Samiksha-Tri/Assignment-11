""" Write a python script to print the octal equivalent of a given decimal number. (do not
use oct() method)"""

n=int(input("enter a number : "))
l1=[]
while n>0:
    rem=n%8
    l1.insert(0,rem)
    n=n//8
for a in l1:
    print(a,end='')    
