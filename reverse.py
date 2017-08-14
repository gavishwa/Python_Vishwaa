#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python
def reverse(no):
    rev=0
    while(no!=0):
        rem=no%10
        rev=rev*10+rem
        no=no//10
    return rev
    
#def main():
#    no=eval(input("Enter the no which you would like to reverse"))
#    print(reverse(no))

#if __name__=='__main__':
#    main()