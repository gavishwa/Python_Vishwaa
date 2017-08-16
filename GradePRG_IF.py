Rating1=input("Enter the Rating")
if Rating1<=5.0 and Rating1!=1.0:
    if Rating1>=4.0 and Rating1<=5.0:
        print("Your Rating is Outstanding")
    elif Rating1>=3.0 and Rating1<4.00:
        print("Your Rating is Excellent")
    elif Rating1>=2.0 and Rating1<3:
        print("Your Rating is Very Good")
    elif Rating1>=1.0 and Rating1<2:
        print("Your Rating is Good")
    else:
        print("Your Rating is Average")
else:
    print("Invalid Entry.Please enter within 1..5 range")



