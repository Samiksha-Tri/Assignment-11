#Write a python script to count digits in a given number
n=int(input("enter a number : "))
c=0
while n>0:
    rem=n%10
    c=c+1
    n=n//10
print("number of digit is: ",c)    
