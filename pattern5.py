def pattern5(no1):
    for i in range(0,no1):
        for j in range(0,no1-i-1):
            print(end=" ")
        for j in range(1,i+1):
            print ("*",end=" ")
        print ("\r")


def main():
    no1=eval(input("Enter the no of Rows"))
    pattern5(no1)

if __name__=='__main__':
    main()

