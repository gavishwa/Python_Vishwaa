#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python
def listmerge2(l1,l2):
#    l1.sort()
#    l2.sort()
    
    for i in range(len(l2)):
        l1.insert(len(l2),l2[i])
        l1.sort()  
    print (l1)

def main():
    l1=eval(input("Enter the Main list"))
    l2=eval(input("Enter the second list"))
    listmerge2(l1,l2)

if __name__=='__main__':
    main()