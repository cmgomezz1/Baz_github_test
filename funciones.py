def obtener_nombre():
    print("Hola Baz")

obtener_nombre()

mensaje = obtener_nombre()
print(mensaje)

def obtener_nombre(name):
    return "Hola Baz. Bienvenido " + name

name = 'Carlos'

print(obtener_nombre(name))

