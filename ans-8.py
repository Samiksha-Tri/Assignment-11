#Write a python script to calculate sum of digits of a given number
n=int(input("enter a number : "))
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
print("sum of digits is: ",sum)    
