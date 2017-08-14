#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python
def listcompare(l1,l2):
#    l1.sort()
#    l2.sort()
    l1.extend(l2)
    l1.sort()  
    print (l1)

def main():
    l1=eval(input("Enter the Main list"))
    l2=eval(input("Enter the second list"))
    listcompare(l1,l2)

if __name__=='__main__':
    main()