def pattern3(no1):
    k=2*no1-2
    for i in range(0,no1):
        for j in range(0,k):
            print (end=" ")
        k = k - 2
        for j in range(0,i+1):
            print ("*",end=" ")
        print("\r")
def main():
    no1=eval(input("Enter the no of Rows"))
    pattern3(no1)

if __name__=='__main__':
    main()

