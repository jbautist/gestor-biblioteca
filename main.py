import os
import funciones


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


while True:
    print('''
    +----------------------------------+
    |            BIBLIOTECA            |
    +----------------------------------+

    Ingresa una opción:

    [1] Ver Libros
    [2] Ver Préstamos
    [3] Nuevo Préstamo
    [4] Quitar Préstamo

    [5] Salir
    ''')

    operacion = input()

    clearConsole()

    if operacion == '1':
        funciones.ver_libros()
    elif operacion == '2':
        funciones.ver_prestamos()
    elif operacion == '3':
        funciones.agregar_prestamo()
    elif operacion == '4':
        funciones.quitar_prestamo()
    elif operacion == '5':
        exit()
    else:
        print('ERROR: has ingresado un carácter o número inválido. Elige una operación del [1] al [4] o ingresa [5] para salir.')
        continue

    ENTER = input('\n[ENTER] Inicio')
    clearConsole()