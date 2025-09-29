x = 5
print(x)
print("hello")


#import pyttsx3
#speaker = pyttsx3.init()
#peaker.say("munnigupta")
#speaker.runAndWait()
#dir(pyttsx3)
student = [
    ["sujal",1111, 'del'] ,
    [ "lali",2222,'mum'] ,
    [ "mummy",3333,'kol'],
]
#op:['sujal', 1111]
print(student[0])
print(student[2][0])
#op:mummy
print(student[2][0][2])
#m
print(len(student))
#3

#print(student[([0][1]:[1][1]:[2][1])])
#student[0:3][1]
print(type(student))
#<class 'list'>
import numpy
#array()
mydb = numpy.array(student)
print(mydb)
print(type(mydb))
#<class 'numpy.ndarray'>
print(mydb[:,1])
['1111' '2222' '3333']

print(mydb[1:3,1:3])
#[['2222' 'mum']
#['3333' 'kol']]

