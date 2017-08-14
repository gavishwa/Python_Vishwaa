#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python
def pattern9(no1):
    c=65
    for i in range(1,no1+1):
        for c in range(65,65+no1,65+i):
            print("%c"%c,end=" ")
        print("\n")
      
def main():
    no1=eval(input("Enter the no of Rows"))
    pattern9(no1)

if __name__=='__main__':
    main()

