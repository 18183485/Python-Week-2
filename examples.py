#var1 = 1
#var2 = 2

#def someFunc(var1):
    #print(f'{var1},{var2}')
#someFunc(3)

#def someFunc(func):
    #print(func(5) + 2)
#someFunc(lambda x: x * 3)

#var1 = 456 % 10
#print(var1)

#A tuple cannot be appended
#var = (1,2,3)
#var.append(4)
#print(var)
# For loop
#for i in range(5):
 #   print(i)


try:
    1/0
except ArithmeticError:
    print('ArithmeticError')
except Exception:
    print('Exception')
except DivisionByZeroError:
    print('DivisionByZero')