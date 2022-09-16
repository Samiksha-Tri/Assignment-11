#Write a python script to calculate factorial of a given number
n=int(input("enter a number : "))
mul=1
for a in range(n,0,-1):
    mul=mul*a
print("factorial is : ",mul)