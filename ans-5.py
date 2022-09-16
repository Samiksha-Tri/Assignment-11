#Write a python script to calculate sum of first N even natural numbers
n=int(input("enter number of even natural numbers you want to sum:"))
sum=0
for a in range(2,n*2+1,2):
    sum=sum+a
print(sum)    