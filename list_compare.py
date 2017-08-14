#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python
def listcompare(l1,l2):
    if len(l1) ==len(l2):
        l1.sort()
        l2.sort()
        for i in range(0,len(l1)):
            if l1[i] !=l2[i]:
                print("Entered List not same")
                break
        else:
            print("Entered List is same")   
    else:
        print("Entered List is not same")

def main():
    l1=eval(input("Enter the Main list"))
    l2=eval(input("Enter the second list"))
    listcompare(l1,l2)

if __name__=='__main__':
    main()