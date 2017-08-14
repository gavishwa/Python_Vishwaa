#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python
import reverse:

def palindrome(no1,no2):
    no2=reverse(no1)
    if no1==no2:
       print("Entered no is Palindrome")
    else:
       print("Entered no is not palindrome")

def main():
    no=eval(input("Enter the no "))
    palindrome(no)

if __name__=='__main__':
    main()