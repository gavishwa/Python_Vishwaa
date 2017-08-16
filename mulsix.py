no1,no2=input("Enter the Lower and Upper number")
sum1=0
for x in range(no1,no2+1,1):
    if x%6==0:
        sum1+=x
print ("The sum of multiple of SIX  from no %d to %d is %d" %(no1,no2,sum1))