import os
tp_numero, nombre_alumno, cont ='- TRABAJO PRACTICO N4 -', 'Geronimo Nuñez', 'PRESIONE ENTER PARA EMPEZAR TP'
ancho_consola = 150
centrado = tp_numero.center(ancho_consola)
centrado2 = nombre_alumno.center(ancho_consola)
centrado3 = cont.center(ancho_consola)
print(centrado)
print(centrado2)
print(centrado3)
input()
# Borrar consola
os.system('cls' if os.name == 'nt' else 'clear')

# Punto 1: Escriba una función que muestre todos los números primos entre 1 y un número n que es ingresado por parámetro.
print('Punto 1: Numeros primos.')
def es_primo(numero):
    for num in range(2, numero):
        
        if numero % num == 0: # Si el numero ingresado es divisible por otro numero que no sea 1 y si mismo, no es primo.
            return False
        return True

n = int(input('Ingrese un numero: '))
for i in range(2, n):
    if es_primo(i):
        print(f'El numero {i} es primo.')

input('\n- ENTER PARA CONTINUAR -\n')

# Punto 2: Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta que el usuario ingrese 
# ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje avisando que ya se agregó el condimento al sándwich.
# Escriba versiones diferentes del programa de acuerdo a estos criterios:
# A: Use un test condicional en el ciclo while para detener la ejecución.
print('Punto 2A: Condimentos ("salir" para terminar)')
def sandwich():
    sanwi = []
    while True:
        cond = input('Ingrese un condimento a su sandwich: ')
        if cond.lower() == 'salir':
            print(f'\nEl sandwich tendra los siguientes condimientos: {sanwi}')
            print('- Fin del punto -')
            break
        else:
            print(f'Se agrego: {cond} al sandwich.')
            sanwi.append(cond)
sandwich()

input('\n- ENTER PARA CONTINUAR -\n')

# B: Use un test condicional dentro del ciclo para decidir si continuar la ejecución.
print('Punto 2B: ')
sanwi_b = []
def sandwich_b():
    cond_b = input('Ingrese un condimento: ')
    print(f'Se agrego {cond_b} al sandwich.')
    sanwi_b.append(cond_b)
    while True:
        opc = input('¿Desea agregar otro condimento? (Si/No): ')
        if opc.lower() == 'si':
            cond_b = input('Ingrese un condimento: ')
            print(f'Se agrego {cond_b} al sandwich.')
            sanwi_b.append(cond_b)
        else:
            print(f'El sandwich tendra los siguientes condimentos: {sanwi_b}')
            print('- FIN DEL PUNTO - ')
            break
sandwich_b()

input('\n- ENTER PARA CONTINUAR -\n')

# Punto 3:
# A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un tamaño 
# y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje 
# describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una
# vez usando argumentos por posición. Llámela una segunda vez usando argumentos por clave.
print('Punto 3A: Remeras.')
def hacer_remera(tamanio, mensaje):
    print(f'\nEl tamaño de la remera sera: {tamanio}.')
    print(f'El mensaje de la remera sera: {mensaje}.')

hacer_remera('2XL', 'VIRTUAL INSANITY')
hacer_remera(tamanio='2XL', mensaje='Dont wanna grow old so I smoke just in case')

input('\n- ENTER PARA CONTINUAR -\n')

# B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por defecto
#  sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los valores
#  por defecto, y la segunda con valores diferentes.
print('Punto 3B: ')
def hacer_remera_b(tamanio, mensaje):
    print(f'\nEl tamaño de la remera sera: {tamanio}.')
    print(f'El mensaje de la remera sera: {mensaje}.')

hacer_remera_b('L', 'Me gusta Python')

tam = input('\nIngrese de que tamaño quiere la remera: (M, L, XL, 2XL): ')
mens = input('Ingrese el mensaje que quiere que tenga su remera: ')
hacer_remera_b(tam, mens)

input('\n- ENTER PARA CONTINUAR -\n')

# Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros de 
# la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo número 
# es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …).

# Lo busque porque no se me caia una idea 
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input('Ingrese un numero para saber su serie Fibonacci: '))
for i in range(num + 1):
    print(f'Fibonacci({i}): {fibonacci(i)}')

input('\n- ENTER PARA CONTINUAR -\n')

# Punto 5 (Opcional) - Calculadora más inteligente: Modifique el ejercicio 9 del primer practico 
# para que la calculadora sea capaz de devolver el resultado solamente de una operación especificada
# por el usuario. Por ejemplo, si el usuario ingresa dos numeros x, y, y luego ingresa ‘1’, la calculadora
# devuelve la suma entre los numeros x,y; si ingresa ‘2’, devuelve la resta, etc.
print('Punto 5: Calculadora.')
def menu():
    print('\n- MENU CALCULADORA-')
    print('1. Suma de los numeros ingresados.')
    print('2. Resta de los numeros ingresados.')
    print('3. Multiplicacion de los numeros ingresados.')
    print('4. Division de los numeros ingresados.')
    print('5. Potenciacion de los numeros ingresados.')
    print('6. Division entera de los numeros ingresados.')
    print('7. Salir.')

def pedir_numeros():
    num1 = float(input('Ingrese el primer numero: '))
    num2 = float(input('Ingrese el segundo numero: '))
    return num1, num2

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    return x / y

def potenciacion(x, y):
    return x ** y

def division_e(x, y):
    return x // y

while True:
    menu()
    opc = int(input('\nIngrese su opcion: '))
    if opc >= 1 and opc <= 6:
        num1, num2 = pedir_numeros()
        if opc == 1:
            print(f'La suma de los numeros es: {suma(num1, num2)}')
        elif opc == 2:
            print(f'La resta de los numeros es: {resta(num1, num2)}')
        elif opc == 3:
            print(f'La multiplicacion de los numeros es: {multiplicacion(num1, num2)}')
        elif opc == 4:
            print(f'La division de los numeros es: {division(num1, num2)}')
        elif opc == 5:
            print(f'La potenciacion de los numeros es: {potenciacion(num1, num2)}')
        elif opc == 6:
            print(f'La division entera de los numeros es: {division_e(num1, num2)}')
    elif opc == 7:
        print('- FIN DEL PUNTO -')
        break
    else:
        print('ERROR. No se encuentra la opcion ingresada. Ingrese una opcion valida.')

input('\n- ENTER PARA CONTINUAR -\n')

# Punto 6 (Opcional) - Conversión imperial: Desarrollar un programa en Python que pueda convertir gramos a libras, 
# centímetros a pulgadas y kilómetros a millas. El programa debe permitir la conversión en ambos sentidos. 
# 1.60934 Km = 1 milla 0.393701 pulgadas = 1 cm 0.00220462 libras = 1 gramo
print('Punto 6: Conversiones imperiales.')
def menu():
    print('\n- MENU CONVERSION IMPERIAL -')
    print('1. Convertir gramos a libras.')
    print('2. Convertir centimetros a pulgadas.')
    print('3. Convertir kilometros a millas.')
    print('4. Salir.')

def pedir_numero():
    numero = float(input('Ingrese un numero para convertir: '))
    return numero

def gramos_libras(num):
    gr_a_lib = num * 0.00220462
    lib_a_gr = num * 453.592
    print(f'Gramos a libras: {gr_a_lib}')
    print(f'Libras a gramos: {lib_a_gr}')

def cm_pulg(num):
    cm_a_pulg = num * 0.393701
    pulg_a_cm = num * 2.54
    print(f'Centimetros a pulgadas: {cm_a_pulg}')
    print(f'Pulgadas a centimetros: {pulg_a_cm}')

def km_mill(num):
    km_a_mill = num * 0.621371
    mill_a_km = num * 1.60934
    print(f'Kilometros a millas: {km_a_mill}')
    print(f'Millas a kilometros: {mill_a_km}')

while True:
    menu()
    opc = int(input('Ingrese una opcion: '))
    if opc >= 1 and opc <= 3:
        numero = pedir_numero()
        if opc == 1:
            gramos_libras(numero)
        elif opc == 2:
            cm_pulg(numero)
        elif opc == 3:
            km_mill(numero)
    elif opc == 4:
        print('- FIN DEL PUNTO -')
        break
    else:
        print('ERROR. Ingrese una opcion valida.')

input('\n- ENTER PARA CONTINUAR -\n')

# Punto 7 (Opcional) - Cuando un año es bisiesto, el mes más corto del año, febrero, tiene 29 días en vez de 28.
# Esto sucede casi cada 4 años. Los tres criterios que permiten saber si un año es bisiesto en el calendario
# gregoriano son los siguientes:
# Si el año es divisible enteramente por 4, es bisiesto a menos que: 
# El año sea divisible por 100, entonces NO es bisiesto, a menos que:
# El año sea también divisible por 400. Entonces sí es un año bisiesto. 
# Esto significa que en el calendario gregoriano los años 2000 y 2400 
# son bisiestos, mientras que los años 1900, 2100, 2200 y 2300 no son bisiestos.

# a) Escriba una función que tome un año y diga si es bisiesto o no.
print('Punto 7A: Años bisiestos.')
def bisiesto(anio):
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        print(f'El año {anio} es bisiesto.')
    else:
        print(f'El año {anio} no es bisiesto.')
        
anio = int(input('Ingrese un año: '))
bisiesto(anio)

input('\n- ENTER PARA CONTINUAR -\n')

# b) Modifique su programa para que devuelva todos los años bisiestos entre el año actual y el año que se pasa a la función 
# como parámetro (este debe ser posterior al año actual).
print('Punto 7B: ')
def bisiesto_entre():
    anio = int(input('Ingrese un año: '))
    while anio <= 2023:
        anio = int(input('Error. Ingrese un año mayor a 2023: '))

    for i in range(2023, anio):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            print(f'El año {i} es bisiesto.')
bisiesto_entre()

input('\n- ENTER PARA CONTINUAR -\n')

# Punto 8 (Opcional) - Si listamos todos los números naturales menores a 10 que son múltiplos de 3 o 5, obtenemos 3,5,6 y 9.
#  La suma de estos múltiplos es 23. Encuentre la suma de todos los múltiplos de 3 o 5 menores a 1000.
print('Punto 8: Multiplos de 3 o 5 menores a 1000.')
def multiplos():
    suma = 0
    for i in range(1001):
        if i % 3 == 0 or i % 5 == 0:
            suma += i
    print(f'La suma de los multiples de 3 o 5 menores a 100 es: {suma}')

multiplos()

print('\n - FIN DEL PROGRAMA - \n')
