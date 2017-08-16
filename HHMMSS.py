HH1,MM1,SS1=input("Enter Valid Time in HH/MM/SS Format")
if HH1>0 and HH1<25:
    if MM1>=0 and MM1<=60:
        if SS1>=0 and SS1<=60:
            print("Time Entered {} {}  {}  is valid".format(HH1,MM1,SS1))

        else:
            print("Seconds Entered =%d is invalid"%SS1)
    else:
        print("Minutes Entered =%d is invalid"%MM1)
else:
    print("Hours Entered =%d is invalid" %HH1)
