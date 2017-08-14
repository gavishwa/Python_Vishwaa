#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python

def numsum(no1):
    results = 0
    while no1 > 0:
        remainder = no1 % 10
        results += (remainder)**3
        no1 = (no1-remainder)/10
    return results
     
def main():
    no1=eval(input("Enter the no you would like to add sum of cubes"))
    print("Entered no of sum of Cubes is %d"%(numsum(no1)))
   
if __name__=='__main__':
    main()


