#Write a python script to calculate sum of cubes of first N natural numbers
n=int(input("enter number of cubes of natural numbers you want to sum:"))
sum=0
for a in range(1,n+1,1):
    sum=sum+(a**3)
print(sum)    