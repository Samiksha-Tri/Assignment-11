# Write a python script to calculate sum of first N odd natural numbers
n=int(input("enter number of odd natural numbers you want to sum:"))
sum=0
for a in range(1,n*2+1,2):
    sum=sum+a
print(sum)    