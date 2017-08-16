#!C:\Python27\python.exe
print ("It's Fun")
def sumofevenodd(lb,ub):
    sum_even=0
    sum_odd=0
    while lb<=ub:
        if lb%2==0:
            sum_even+=lb
        else:
            sum_odd+=lb
        lb+=1
    return sum_even,sum_odd
if __name__=="__main__":
    lb,ub=input("Enter the Lower and Upper Bound")
    r1,r2=sumofevenodd(lb,ub)
    print(r1,r2)


