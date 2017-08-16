def VariableArgsAdd(a1,b1):
    sum=0
    for x in args:
        sum+=x
    print(sum)
VariableArgsAdd(10,20,30)
VariableArgsAdd(10,20,30,50,70.0,90)