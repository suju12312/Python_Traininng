## 02


python is a interpreter language

to creatwe a file 
notepad myfirst.py (this fioe is stored in hard dsk so we can share and doenall extrea stuff)

python myfirst.py


but we used ide like vs code

jupyter notebook

whichever os i am on now suppose window so run there command
system("notepad)
system("chrome")
print("hello")
print is a function that print on screen
function:
has print , whatsapp , emaqil,textmesage,printer and hardcopy of page , connect to speaker  , sms

program files (hd) == module inside this function s there

file come from software in python soft == libraries

library ---- program fle -- func

how to install software in python?
pip

suppose we have to do text to speech from speaker like hello
PS C:\Users\Sujal_laptop\Python_Traininng> notepad
PS C:\Users\Sujal_laptop\Python_Traininng> pip install pyttsx3
Defaulting to user installation because normal site-packages is not writeable
Collecting pyttsx3
  Downloading pyttsx3-2.99-py3-none-any.whl.metadata (6.2 kB)
Collecting comtypes (from pyttsx3)
  Downloading comtypes-1.4.12-py3-none-any.whl.metadata (7.3 kB)
Collecting pypiwin32 (from pyttsx3)
  Downloading pypiwin32-223-py3-none-any.whl.metadata (236 bytes)
Collecting pywin32 (from pyttsx3)
  Downloading pywin32-311-cp313-cp313-win_amd64.whl.metadata (10 kB)
Downloading pyttsx3-2.99-py3-none-any.whl (32 kB)
Downloading comtypes-1.4.12-py3-none-any.whl (253 kB)
Downloading pypiwin32-223-py3-none-any.whl (1.7 kB)
Downloading pywin32-311-cp313-cp313-win_amd64.whl (9.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.5/9.5 MB 3.9 MB/s  0:00:02
Installing collected packages: pywin32, pypiwin32, comtypes, pyttsx3
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 0/4 [pywin32]  WARNING: The scripts pywin32_postinstall.exe and pywin32_testall.exe are installed in 'C:\Users\Sujal_laptop\AppData\Roaming\Python\Python313\Scripts' which is not on PATH. 
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location. 
   ━━━━━━━━━━━━━━━━━━━━╺━━━━━━━━━━━━━━━━━━━ 2/4 [comtypes]  WARNING: The script clear_comtypes_cache.exe is installed in 'C:\Users\Sujal_laptop\AppData\Roaming\Python\Python313\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location. 
Successfully installed comtypes-1.4.12 pypiwin32-223 pyttsx3-2.99 pywin32-311
PS C:\Users\Sujal_laptop\Python_Traininng> 

libraries give us modules (import)
every module gives a function


python ------- connect speaker (device)

#string to speaker : speak:tts
pip install pyttsx3


task:  python code to sewnd whatsaaapcode
create pytyhon code text to phone number
create pyhon cod to send emails
create pytyon code -- control featue of speaker

list
nested list
1d === vector
2d data == matrix
student = [
    ["sujal",1111, 'del'] ,
    [ "lali",2222,'mum'] ,
    [ "mummy",3333,'kol'],
]
questin is that print second column
print(student[([0][1]:[1][1]:[2][1])]) this is not allow maine jho0 bhi kiya yeha 
list is not meant for column wise operations

import numpy
#array()
mydb = numpy.array(student)
print(mydb)
print(type(mydb))
#<class 'numpy.ndarray'>
print(mydb[:,1])
we can do this by array importing by numpy to find only column 
