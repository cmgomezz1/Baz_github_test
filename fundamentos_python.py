# Datos del usuario
edad = 30
nombre = 'Carlos'
Apellido = 'Gómez'
print(nombre, Apellido, edad) 

# Operaciones básicas
x = 20
y = 10
print("Estas son operaciones aritmeticas")
print(x + y)
print(x - y)
print(x / y)
print(x * y)
print(x // y)

# Operador de Módulo
print("\n")
print("Esto es la utilización del operador de módulo")
print(15 % 3)

# Estructuras de datos
nombres_baz = ['Ricardo', 'Bety', 'Roberto', 'Carlos', 'Gonzalo', 'Lety', 'Lore']
nuevos_nombres = []
print("Estos son los nombres del equipo de QA Baz")
print(nombres_baz)

# Índices
print(nombres_baz[2])

# Slices
print(nombres_baz[0:4])
print(nombres_baz[0:6:2])

# Añadir valores a una lista
nuevos_nombres.append('Lucia')
print(nuevos_nombres)

#Tuplas
nombres_estudiantes = ('Hugo', 'Paco', 'Luis')
print(nombres_estudiantes[1])

# Diccionario
carros = {
    'carro_01': {'Marca': 'Toyota', 'Modelo': '2018'},
    'carro_02': {'Marca': 'Nissan', 'Modelo': '2020'},
    'carro_03': {'Marca': 'BMW', 'Modelo': '2023'}
}
print(carros['carro_02']['Modelo'])

print(carros.keys())
print(carros.values())
print(carros.items())

