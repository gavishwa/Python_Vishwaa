#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python
def pattern10(no1):
    c=65
    ch=chr(c)
    for i in range(0,no1):
        k=k+2
        for j in range(0,k,-1):
            print("\t",end=" ")
            ch=chr(c)
        for j in range(0,no1):
            print(ch)
        c=c+1
        print("\n")
      
def main():
    no1=eval(input("Enter the no of Rows"))
    pattern10(no1)

if __name__=='__main__':
    main()

