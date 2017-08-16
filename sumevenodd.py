no1,no2=input("Enter the Lower and Upper number")
evensum1=0
oddsum1=0
for x in range(no1,no2+1,1):
    if x%2==0:
       evensum1+=x
    else: oddsum1+=x
print("Thei  of EVEN No from no %d to %d is %d" %(no1,no2,evensum1))
print ("The sum of ODD No from no %d to %d is %d" %(no1,no2,oddsum1))
