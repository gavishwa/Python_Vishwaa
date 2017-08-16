def outerfunction(msg):
    message = msg
    def innerfunction():
        print (message)
    return innerfunction
hi_func = outerfunction('Hi')
bye_func = outerfunction('Bye')
hi_func()
bye_func()
