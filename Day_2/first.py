#aap kase ho
#
#c:\Users\Sujal_laptop\Python_Traininng\Day_2\first.py"
#  File "c:\Users\Sujal_laptop\Python_Traininng\Day_2\first.py", line 1
 #   aap kase ho
  #      ^^^^
#SyntaxError: invalid syntax


print("hello wolrld")
#op: hello wolrld

city = "jaipur"
print(city)



name = "sujal"

python = ["arun" ,"harhsh", "rahul"]
print(python)
#op: ['arun', 'harhsh', 'rahul']
#      0         1           --> index
print(type(python))
#op:<class 'list'>

print(python[1]) #index 
python.append("sujal") #variable name . functionality
print(python)
#['arun', 'harhsh', 'rahul', 'sujal'] 
print(len(python))
print(python[0:2])
#p : ['arun', 'harhsh']

print(python[:4])
#op: ['arun', 'harhsh', 'rahul', 'sujal']

print("rahul" in python)
#True


print(type("rahul" in python))
#op:<class 'bool'>

print(python[-1])
#op:sujal

print(python[::-1])

print(dir(python))
#op:  ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
python.reverse()
print(python)
#op : ['sujal', 'rahul', 'harhsh', 'arun']
python.insert(2,"pop")
print(python)
#op: ['sujal', 'rahul', 'pop', 'harhsh', 'arun']

