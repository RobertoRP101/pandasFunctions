# help()

def hello(digit):
    return f'{digit}.- Hello world'
    
digit_list = [x for x in range(1,11,1)]    

print(list(map(hello, digit_list)))