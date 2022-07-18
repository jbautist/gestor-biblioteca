import os
from datetime import datetime  
from datetime import timedelta
import db_connection as sql


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def ver_libros_genero():
    '''Muestra todos los valores de las columnas:
    "book_id" y "title"
    de la tabla "books" 
    de la base de datos "biblioteca.db" 
    ordenado por "genre_id".
    '''  

    libros = sql.dql('biblioteca.db', 
    '''SELECT books.book_id, books.title, genres.name  
    FROM books
    JOIN genres
    ON books.genre_id = genres.genre_id
    ORDER BY books.genre_id;
    ''')
    
    genero = None
    for registro in libros:
        id, title, genre = registro
        if genero != genre:
            print('\n', genre.upper())
            genero = genre
        print(f'        [{id}] {title}')


def ver_libros_autor():
    '''Muestra todos los valores de las columnas:
    "book_id" y "title"
    de la tabla "books" 
    de la base de datos "biblioteca.db" 
    ordenado por "author_id".
    '''    

    libros = sql.dql('biblioteca.db', 
    '''SELECT books.book_id, books.title, authors.name  
    FROM books
    JOIN authors
    ON books.author_id = authors.author_id
    ORDER BY books.author_id;
    ''')
    
    autor = None
    for registro in libros:
        id, title, author = registro
        if autor != author:
            print('\n', author.upper()) 
            autor = author
        print(f'             [{id}] {title}')


def ver_libros():
    '''Proporciona 2 opciones para mostrar los libros y ejecuta la función de la opción seleccionada.'''  

    while True:
        print('''
        Elija el método de búsqueda:

        [1] Ver por género
        [2] Ver por autor
        ''')
        opcion = input()
        clearConsole()
        if opcion == '1':
            ver_libros_genero()
            break
        elif opcion == '2':
            ver_libros_autor()
            break
        else:
            print('ERROR: has ingresado un carácter o número inválido. Por favor elige una operación: [1] o [2].')


def comprobar_disponibilidad(id_libro):
    '''Comprueba si la consulta SELECT devuelve un valor.

    Args:
        id_libro (str): Un valor del "1" al "30".

    Returns:
        bool: True si la consulta devolvió un valor, sino False.
    '''    

    disponibilidad = sql.dql('biblioteca.db', 
    f'''SELECT copie_id
    FROM copies 
    WHERE book_id = {id_libro}
    AND borrower_id IS NULL
    LIMIT 1;
    ''')
    return bool(disponibilidad)


def agregar_prestamo():
    '''Registra nuevos préstamos de libros en las tablas "borrowers", "loans" y "copies"
    en la base de datos "biblioteca.db".

    1)Bucle while: el usuario elige el libro a prestar.
    2)Sentencia if: comprueba que haya una copia disponible del libro elegido.
    3)Bucle while: solicita los datos del pretatario para registar en la base de datos.
    4)Registra el prestamo insertando los datos en las tablas: "borrowers", "loans" y 
    actualizando la tabla "copies".
    '''    

    #Creando set con números del 1 al 30 de tipo string.
    ids_libros = set([str(x) for x in range(1, 31)])
    #Eligiendo libro a prestar.
    while True:
        ver_libros()
        id_libro = input(('\nIngrese [ID] del libro o [X] para cancelar: '))
        clearConsole()
        if id_libro in ids_libros:
            break
        elif id_libro.upper() == 'X':
            return
        else:
            print('ERROR: has ingresado un carácter o número inválido.')
    
    if comprobar_disponibilidad(id_libro) == False:
        print('No hay copias disponibles del libro elegido.')
        return
    
    #Solicitud de datos del prestatario.
    while True:
        print('Ingrese los datos del prestatario:\n')
        nombre = input('NOMBRE: ')
        direccion = input('DIRECCIÓN: ')
        telefono = input('TELÉFONO: ')
        clearConsole()
        #Comprobando que el dato "telefono" ingresado sea válido.
        if not telefono.isnumeric():
            print('ERROR: ingresa un TELÉFONO válido.\n')
        else:
            break
        
    #Almacenamiento de los datos en las tablas: "borrowers", "copies" y "loans".
    #Tabla: "borrowers"
    sql.dml('biblioteca.db', 
    '''INSERT INTO borrowers 
    (name, address, phone) VALUES (?, ?, ?);
    ''', (nombre, direccion, telefono))
    id_prestatario = sql.dql('biblioteca.db', f'SELECT borrower_id FROM borrowers WHERE name ="{nombre}";')
    id_prestatario = id_prestatario[0][0]

    #Tabla: "copies"
    sql.dml('biblioteca.db',
    f'''UPDATE copies 
    SET borrower_id = {id_prestatario}
    WHERE copie_id = (SELECT copie_id FROM copies WHERE book_id = {id_libro} AND borrower_id IS NULL 
    LIMIT 1);
    ''')
    id_copia = sql.dql('biblioteca.db', f'SELECT copie_id FROM copies WHERE borrower_id = {id_prestatario} AND book_id = {id_libro};')
    id_copia = id_copia[0][0]

    #Tabla: "loans"
    fecha = datetime.today().strftime('%d-%m-%y')
    vencimiento = (datetime.today() + timedelta(days=30)).strftime('%d-%m-%y')
    sql.dml('biblioteca.db', 
    '''INSERT INTO loans
    (borrower_id, copie_id, deliver_date, expiration_date) VALUES (?, ?, ?, ?);
    ''', (id_prestatario, id_copia, fecha, vencimiento))
    titulo_libro = sql.dql('biblioteca.db', f'SELECT title FROM books WHERE book_id = {id_libro};')
    titulo_libro = titulo_libro[0][0]

    print(f'''El préstamo del libro ha sido registrado con éxito:
    PRESTATARIO: {nombre}
    LIBRO: {titulo_libro}
    ID DE LA COPIA: {id_copia}
    FECHA: {fecha}
    VENCIMIENTO: {vencimiento}''')


def ver_prestamos():
    '''Muestra todos los datos de las columnas: "load_id", "name", "title", "copie_id", "deliver_date" y "expiration_date"
    de las tablas: "copies", "borrowers", "loans" y "books"
    de la base de datos "biblioteca.db"
    ordenado por "expiration_date".
    '''    

    prestamos = sql.dql('biblioteca.db',
    '''SELECT loans.loan_id, borrowers.name, books.title, copies.copie_id, loans.deliver_date, loans.expiration_date
    FROM copies
    INNER JOIN borrowers ON copies.borrower_id = borrowers.borrower_id
    INNER JOIN loans ON copies.borrower_id = loans.borrower_id
    INNER JOIN books ON copies.book_id = books.book_id
    ORDER BY loans.expiration_date;
    ''')
    
    if bool(prestamos) == False:
        print('No hay préstamos resgistrados en la base de datos.')
        return

    for prestamo in prestamos:
        prestamo, nombre, titulo_libro, id_copia, fecha, vencimiento = prestamo
        print(f'''
        PRÉSTAMO N°: {prestamo}
        PRESTATARIO: {nombre}
        LIBRO: {titulo_libro}
        ID DE LA COPIA: {id_copia}
        FECHA: {fecha}
        VENCIMIENTO: {vencimiento}
        ''')


def quitar_prestamo():
    '''Elimina préstamos de libros eliminando registros de las tablas "borrowers" y "loans" 
    y actualizando la tabla "copies" 
    de la base de datos "biblioteca.db".
    '''   

    '''Cosultando todos los datos de la columna "loan_id" de la tabla "loans",
    convirtiendolos a tipo str y almacenadolos en un set.
    '''
    datos = sql.dql('biblioteca.db', 'SELECT loan_id FROM loans;')

    if bool(datos) == False:
        print('No hay préstamos resgistrados en la base de datos.')
        return

    numeros_prestamos = set()
    for tupla in datos:
        for numero in tupla:
            numeros_prestamos.add(str(numero))

    numero_prestamo = input('Ingrese el número del préstamo a eliminar o [X] para cancelar: ')
    clearConsole()

    if numero_prestamo in numeros_prestamos:
        datos_prestatario = sql.dql('biblioteca.db', 
        f'''SELECT loans.borrower_id, borrowers.name
        FROM loans 
        INNER JOIN borrowers ON loans.borrower_id = borrowers.borrower_id
        WHERE loan_id = {numero_prestamo};''')
        id_prestatario, nombre_prestatario = datos_prestatario[0]

        sql.dml('biblioteca.db', f'UPDATE copies SET borrower_id = NULL WHERE borrower_id = {id_prestatario};')
        sql.dml('biblioteca.db', f'DELETE FROM loans WHERE borrower_id = {id_prestatario};')
        sql.dml('biblioteca.db', f'DELETE FROM borrowers WHERE borrower_id = {id_prestatario};')

        print(f'El préstamo número {numero_prestamo} y el prestatario {nombre_prestatario} han sido eliminados de la base de datos.')
    elif numero_prestamo.upper() == 'X':
        return
    else:
        print('ERROR: préstamo inválido.')