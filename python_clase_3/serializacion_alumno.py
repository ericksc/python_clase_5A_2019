# ejemplo creación de una clase
class Alumno:
    def __init__(self, nombre_completo, titulo, edad):
        self.apellidos = nombre_completo['apellidos']
        self.nombre = nombre_completo['nombre']
        self.titulacion = titulo
        self.edad = edad

    def __repr__(self):
        return repr([self.nombre, self.apellidos, self.titulacion, self.edad])

nombre_completo = {'apellidos': 'Salas Chaverri', 'nombre': 'Erick'}
erick = Alumno(nombre_completo, 'ing', 20)

#print(erick)

import pickle

clase_python = []
clase_python.append(erick)

with open('clase_python.p', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(clase_python, f, pickle.HIGHEST_PROTOCOL)

with open('clase_python.p', 'rb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    clase_python_updated = pickle.load(f)

print(clase_python_updated)