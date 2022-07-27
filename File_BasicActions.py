import os
import datetime
file=open('Sirve.txt','w')
file.write('Esperemos que esto sirva')
file.close()



print(os.getcwd())   
print(os.path.abspath('Sirve.txt'))
print(os.path.getsize('Sirve.txt'))

#Para mostrar la ultima modificacion
fecha=os.path.getmtime('Sirve.txt')
print(datetime.datetime.fromtimestamp(fecha))


#Crea un directorio (mk) y te cambias a un directorio (ch)
os.mkdir('Dir_1')
print(os.getcwd())
# # os.chdir('Dir_1')
# # print(os.getcwd())

#Eliminas directorio (rm), para que funcione no puedes estar dentro del directorio que vas a eliminar
os.mkdir('Dir_2')
os.rmdir('Dir_1')
