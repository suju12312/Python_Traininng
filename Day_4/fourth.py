s = "ring"
print(s)
d = True
print(type(d)) #<class 'bool'>
x=5
import sys 
print(sys.getsizeof(x)) #28

phone = [1,2,3,4,5]
print(sys.getsizeof(phone)) #104

#tuple
newphone = (1,2,3,4,5)
print(sys.getsizeof(newphone)) #80


a=10
b=20
#swap operation
a,b = b,a
print(a,b)  #20 10

age = 23
name ="vimal"
#f-string approach
print(f"hey my nme is {name} and age is {age}")
#hey my nme is vimal and age is 23
print(f"hey my nme is {name=} and age is {age=}")
#hey my nme is name='vimal' and age is age=23
