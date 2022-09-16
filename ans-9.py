"""Write a python script to print binary equivalent of a given decimal number. (do not
use bin() method)"""

n=int(input("enter a number : "))
l1=[]
while n>0:
    rem=n%2
    l1.insert(0,rem)
    n=n//2
for a in l1:
    print(a,end='')    
