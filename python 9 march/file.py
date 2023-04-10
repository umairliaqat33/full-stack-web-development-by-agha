# print('hello world!!')
# if(6>5):
#     print("six is greater than five")
#     if(5>4):
#         print("five is greater than four")

# i=6
# y="This is python's lab session"
# print(i)
# print(y)
# i=int(20)
# j=str("Hello world using data type specification")
# k=float(44.2)
# print(i,j,k)

# x,y,z='Hello world',"323","chl by chl"
# print(x,y,z)

# x=y=z='Hello world'
# print(x,y,z)

# x='Welcome'
# y='to'
# z='class'
# i=x,y,z
# print(i)
# print(x,y,z)

# i='this is our global variable outside the function'
# def myFunc():
#     print("I am inside function and printing the variable: "+i)

# myFunc()

# i=str('i am a string')
# j=int(45)
# k=float(10.2)
# # print(i,j,k)
# # print(i[0])
# print(i[3:len(i)-3])

# s=str('i am going to be modified')
# s=s.upper()
# print(s)

# s=str('i am going to be modified')
# print(s.removeprefix('i'))
# print(s.replace('i',''))

# List
# list=['Umair','Liaqat']
# print(list)
# print(list[1])
# print(len(list))
# print(list.remove('Umair'))
# list.append('Ali')
# print(list)
# list.sort()
# print(list)

# Tuple
# tuple=('Umair', 'Liaqat')
# print(tuple)

# dictionary
# dict={
#     'name':'Umair',
#     'fName':'Liaqat'
# }
# print(dict)
# print(dict['name'])

# If-else if-else
# a=200
# b=100
# if(b>a):
#     print('b is greater than a')
# elif(a==b):
#     print('a is equal to b')
# else:
#     print('a is greater than b')

# looping
# list=['a','b','c','d']
# for j in list:
#     print(j)

# classes
class Person:
# constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age

person1=Person('Umair',12)
print(person1.age)
print(person1.name)