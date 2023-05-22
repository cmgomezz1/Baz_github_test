# Ciclo FOR
names = ['Hugo', 'Paco', 'Luis']
absence = []

for name in names: 
    #print(name)
    if name == 'Paco':
        print(name + " si se encuentra en clase")
    else: 
        absence.append(name)

print("\n")
print("Esta es la lista de alumnos ausentes")
print(absence)   
print("\n") 


#Ciclo while
i = 1
while i < 8:
    print(i)
    if i == 4:
        break
    i += 1

print("\n")

# age = 23
#     if age < 4: 
#         ticket_price = 0
#     elif age < 18:
#         ticket_price = 10
#     else:
#         ticket_price = 15

# print("El precio del ticket es de ")
# print(ticket_price)

print("\n")


def evaluacion_edad(age):
    if age < 4: 
        ticket_price = 0
    elif age < 18:
        ticket_price = 10
    else:
        ticket_price = 15

    print("El precio del ticket es de ")
    print(ticket_price)

age = int(input("Por favor ingresa tu edad:"))
evaluacion_edad(age)
