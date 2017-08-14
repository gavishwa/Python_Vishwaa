def pattern7(no1):
    for i in range(0,no1):
        for j in range(0,no1-i-1):
            print ("\t",)
        for j in range(0,2*i+1):
            print ("*\t",)
        print ("\n")

def main():
    no1=eval(input("Enter the no of Rows"))
    pattern7(no1)

if __name__=='__main__':
    main()

