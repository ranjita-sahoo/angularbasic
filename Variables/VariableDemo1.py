# Value Type; (int, string, float, char, boolean, tuple)
# Reference Type (list, dicionary, class)

# Whole number (int)
# Real Number (float)
# text (string)
# collections (list, tuples, set, dictionary)

# int x = 10

x = 10
y = 20
print(x)
print('The value of x is :' + str(x)) # type casting
print('The value of x is : ', x)
print('The value of x is : , The value of y is : ',x,y)
print('The value of x is : {}, The value of y is : {}'.format(x,y))
print('The value of x is : {1}, The value of y is : {0}'.format(x,y))
print('The value of x is : %d, The value of y is : %d' % (x,y))

print("The tpe of x is : ", type(x))

print("......")
a = int(input("enter the value1:"))
b = int(input("enter the value2:"))
print("the value of a is:{},the value of b is{}".format(a,b))