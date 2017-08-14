#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python
def list_union(l1,l2):
    l1.sort()
    l2.sort()
    l3=[]
    for element in l1:
	    l3.append(element)
    for element in l2:
    	if element not in l3:
            l3.append(element)
    l3.sort()  
    print (l3)

def main():
    l1=eval(input("Enter the Main list"))
    l2=eval(input("Enter the second list"))
    list_union(l1,l2)

if __name__=='__main__':
    main()