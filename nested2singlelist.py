#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python
def nested2singlelist(l1):
    l2=[]
    for item in l1:
        if isinstance(item,list):
            for subitem in item:
                l2.append(subitem)
        else:
            l2.append(item)
    print (l2)
def main():
    l1=eval(input("Enter the Main list"))
    nested2singlelist(l1)
if __name__=='__main__':
    main()