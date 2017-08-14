#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python
def elementcount(l1,c1):
    count=0
    for i in range(0,len(l1)):
        if l1[i] ==c1:
            count=count+1

    print("Count is %d" %count)   


def main():
    l1,c1=eval(input("Enter the Main list and Char to count"))
    elementcount(l1,c1)

if __name__=='__main__':
    main()