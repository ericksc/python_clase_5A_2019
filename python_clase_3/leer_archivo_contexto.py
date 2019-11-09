# esto es un ejemplo para leer archivos con with

with open('my_file.txt') as f:
    datos = f.readlines()
# note que no ocupamos el close
print(datos)
print('esta es la primera linea' , datos[0])