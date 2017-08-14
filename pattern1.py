#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python
def pattern1(no1):
    for i in range(1,no1+1):
        for j in range(1,i+1):
            print("*",end="")
#       print("*\t",end=")
        print("\n")
      
def main():
    no1=eval(input("Enter the no of Rows"))
    pattern1(no1)

if __name__=='__main__':
    main()
