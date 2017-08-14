def pattern6(no1):
    for i in range(0,no1):
        for j in range(1,no1+1-i):
            print ("*",end=" ")
        print ("\r")
        for j in range(0,i+1):
            print(end=" ")
def main():
    no1=eval(input("Enter the no of Rows"))
    pattern6(no1)

if __name__=='__main__':
    main()

