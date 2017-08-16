no1=input("Enter the  number")
sum=0
i=0
while i<=no1:
    if i%2==0:
      sum+=i
    i+=1
print("The Sum of %d Even number from 0 is %d"%(no1,sum))