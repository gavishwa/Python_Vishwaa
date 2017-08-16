def VariableArgsAdd(*args):
    print (type(args))
    for x in args:
	print(x)
VariableArgsAdd(10,20,30)
VariableArgsAdd(10,20,30,50,70,90)