#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python

def minmax(l1):
   
    max=min=l1[0]
    i=1
    while i<len(l1):
        if (l1[i] > max):
            max=l1[i]
        if l1[i]<min:
            min=l1[i]
        i+=1
    print("Min no %d" %min)
    print("Max no %d" %max)
    return max,min

        
  
def main():
    l1=eval(input("Enter the list to identify the Min and Max"))
    minmax(l1)

if __name__=='__main__':
    main()        
    
