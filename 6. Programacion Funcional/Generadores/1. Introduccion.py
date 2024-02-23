from os import system

def generador():
    yield array[0]
    yield array[1]
    yield array[2]
    yield array[3]
    yield array[4]

system('cls')

gen = generador()

array = [2, 4, 5, 3, 1]
print(f"La lista es {array}")
for i in range(len(array)):
    print(f"posición {i}: {next(gen)}")