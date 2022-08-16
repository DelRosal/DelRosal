#LIBRARIES
import os
import datetime

#CREATE FILE AND WRITE TEXT
file=open('Example.txt','w')
file.write('Esperemos que esto sirva')
file.close()

#OBTAIN FILE INFO
print(os.getcwd())   
print(os.path.abspath('Sirve.txt'))
print(os.path.getsize('Sirve.txt'))

#SHOW LAST MODIFICATION
fecha=os.path.getmtime('Sirve.txt')
print(datetime.datetime.fromtimestamp(fecha))

#CREATE DIRECTORY
os.mkdir('Dir_1')
print(os.getcwd())

#CHANGE DIRECTORY
os.chdir('Dir_1')
print(os.getcwd())

#REMOVE DIRECTORY
os.rmdir('Dir_1')

#MODIFY FILE
with open ("Example.txt","w") as file:
    file.write("")

