#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python
def GCD(no1,no2):
    while no1!=no2:
        if no1<no2:
            no2=no2-no1
        else:
            no1=no1-no2
    return no1
def main():
    no1,no2=eval(input("Enter two numbers to identify the GCD"))
    result=GCD(no1,no2)
    print ("The GCD for the Entered numbers %d" %result)
if __name__=='__main__':
    main()
