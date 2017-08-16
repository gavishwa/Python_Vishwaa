def primeno(no):
    for i in range(2,no):
        if no % i  == 0:
            return True
        else:
            return False
no1=input("Enter the no to validate")
if primeno(no1):
    print "%d is a prime number!" %no1
else:
    print "%d is NOT a prime number!" % no1


