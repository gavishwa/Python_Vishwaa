#!C:\Users\varunachalam\AppData\Local\Programs\Python\Python36-32\python
import sumofcubes1
    
def main():
    no1=eval(input("Enter the no you would like to Check whether this is Armstrong no"))
    no2=sumofcubes1.sumcubes(no1)
    if no1==no2:
        print("Entered no %d is Armstrong no"%(no1))
    else:
        print("Entered no %d is Not Armstrong no"%(no1))
if __name__=='__main__':
    main()

