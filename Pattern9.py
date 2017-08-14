#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python
def pattern10(no1):
    c=65
    for i in range(0,no1):
        for j in range(0,i+1):
            ch=chr(c)
            print(ch,end=" ")
        c=c+1
        print("\n")
      
def main():
    no1=eval(input("Enter the no of Rows"))
    pattern10(no1)

if __name__=='__main__':
    main()

