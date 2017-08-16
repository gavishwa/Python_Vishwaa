date1,month1,year1=input("Enter Valid Date in DD MM YY Format")
if date1>0 and date1<32:
    if month1>0 and month1<13:
        if year1>0:
            print("Date {} {}  {}  is valid".format(date1,month1,year1))

        else:
            print("YY=%d is invalid"%year1)
    else:
     print("MM=%d is invalid"%month1)
else:
    print("dd=%d is invalid" %date1)
