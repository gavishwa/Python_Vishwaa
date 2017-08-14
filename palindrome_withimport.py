#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python
import reverse
def palindrome(no1):
    no2=reverse(no1)
    if no1==no2:
        print("Entered no is Palindrome")
    else:
        print("Entered no is not Palindrome")
def main():
    no1=input("Enter the no")
    print(palindrome(no1))
if __name__=='__main__':
    main()
