sum=1
for i in range(1,101):
    if i%5==0:
       continue
    sum+=i
    print("The sum %d is %d" %(i,sum))
