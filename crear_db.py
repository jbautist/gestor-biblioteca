import db_connection as sql


sql.ddl('biblioteca.db', 
'''--Creando tablas.

CREATE TABLE genres (
  genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT
);

CREATE TABLE authors (
  author_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT
);

CREATE TABLE books (
  book_id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  genre_id INTEGER,
  author_id INTEGER
);

CREATE TABLE copies (
  copie_id INTEGER PRIMARY KEY AUTOINCREMENT,
  book_id INTEGER,
  borrower_id INTEGER
);

CREATE TABLE loans (
  loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
  borrower_id INTEGER,
  copie_id INTEGER,
  deliver_date TEXT,
  expiration_date TEXT
);

CREATE TABLE borrowers (
  borrower_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  address TEXT,
  phone INTEGER
);


/*Insertando registros en:
  genres
  authors
  books
  copies.*/

INSERT INTO genres (name) VALUES ('Infantil | Juvenil');
INSERT INTO genres (name) VALUES ('Mágico');
INSERT INTO genres (name) VALUES ('Policíaco');
INSERT INTO genres (name) VALUES ('Aventura');
INSERT INTO genres (name) VALUES ('Ficción');
INSERT INTO genres (name) VALUES ('Fantasía');
INSERT INTO genres (name) VALUES ('Manual | Autoayuda');
INSERT INTO genres (name) VALUES ('Histórico');
INSERT INTO genres (name) VALUES ('Drama');

INSERT INTO authors (name) VALUES ('Lucy Maud Montgomery');
INSERT INTO authors (name) VALUES ('Gabriel García Márquez');
INSERT INTO authors (name) VALUES ('Agatha Christie');
INSERT INTO authors (name) VALUES ('Miguel de Cervantes Saavedra');
INSERT INTO authors (name) VALUES ('Paulo Coelho');
INSERT INTO authors (name) VALUES ('J. R. R. Tolkien');
INSERT INTO authors (name) VALUES ('Antoine de Saint-Exupéry');
INSERT INTO authors (name) VALUES ('Dan Brown');
INSERT INTO authors (name) VALUES ('J. D. Salinger');
INSERT INTO authors (name) VALUES ('C. S. Lewis');
INSERT INTO authors (name) VALUES ('Dr. Benjamin Spock');
INSERT INTO authors (name) VALUES ('H. Rider Haggard');
INSERT INTO authors (name) VALUES ('J.K. Rowling');
INSERT INTO authors (name) VALUES ('Johanna Spyri');
INSERT INTO authors (name) VALUES ('Charles Dickens');
INSERT INTO authors (name) VALUES ('Lewis Carroll');
INSERT INTO authors (name) VALUES ('Arthur Conan Doyle');
INSERT INTO authors (name) VALUES ('Vladimir Nabokov');
INSERT INTO authors (name) VALUES ('Robert James Waller');
INSERT INTO authors (name) VALUES ('Napoleón Hill');
INSERT INTO authors (name) VALUES ('Cao Xueqin');
INSERT INTO authors (name) VALUES ('Louise Hay');
INSERT INTO authors (name) VALUES ('Julio Verne');

INSERT INTO books (title, genre_id, author_id) VALUES ('Ana la de Tejas Verdes', 1, 1);
INSERT INTO books (title, genre_id, author_id) VALUES ('Cien años de Soledad', 2, 2);
INSERT INTO books (title, genre_id, author_id) VALUES ('Diez Negritos', 3, 3);
INSERT INTO books (title, genre_id, author_id) VALUES ('Don Quijote de la Mancha', 4, 4);
INSERT INTO books (title, genre_id, author_id) VALUES ('El Alquimista', 5, 5);
INSERT INTO books (title, genre_id, author_id) VALUES ('El Hobbit', 6, 6);
INSERT INTO books (title, genre_id, author_id) VALUES ('El Principito', 1, 7);
INSERT INTO books (title, genre_id, author_id) VALUES ('El Código Da Vinci', 3, 8);
INSERT INTO books (title, genre_id, author_id) VALUES ('El Guardián Entre El Centeno', 5, 9);
INSERT INTO books (title, genre_id, author_id) VALUES ('El León, la Bruja Y El Armario', 4, 10);
INSERT INTO books (title, genre_id, author_id) VALUES ('El Libro Del Sentido Del Común Del Cuidado de Bebés Y Niños', 7, 11);
INSERT INTO books (title, genre_id, author_id) VALUES ('El Señor de Los Anillos', 6, 6);
INSERT INTO books (title, genre_id, author_id) VALUES ('Ayesha: El Retorno de Ella', 4, 12);
INSERT INTO books (title, genre_id, author_id) VALUES ('Harry Potter y El Cáliz de Fuego', 6, 13);
INSERT INTO books (title, genre_id, author_id) VALUES ('Harry Potter y El Misterio Del Príncipe', 6, 13);
INSERT INTO books (title, genre_id, author_id) VALUES ('Harry Potter y El Prisionero de Azkaban', 6, 13);
INSERT INTO books (title, genre_id, author_id) VALUES ('Harry Potter y La Cámara Secreta', 6, 13);
INSERT INTO books (title, genre_id, author_id) VALUES ('Harry Potter y La Orden Del Fénix', 6, 13);
INSERT INTO books (title, genre_id, author_id) VALUES ('Harry Potter y La Piedra Filosofal', 6, 13);
INSERT INTO books (title, genre_id, author_id) VALUES ('Harry Potter y Las Reliquias de la Muerte', 6, 13);
INSERT INTO books (title, genre_id, author_id) VALUES ('Heidi', 1, 14);
INSERT INTO books (title, genre_id, author_id) VALUES ('Historia de Dos Ciudades', 8, 15);
INSERT INTO books (title, genre_id, author_id) VALUES ('Las Aventuras de Alicia en el País de las Maravillas', 1, 16);
INSERT INTO books (title, genre_id, author_id) VALUES ('Las Aventuras de Sherlock Holmes', 3, 17);
INSERT INTO books (title, genre_id, author_id) VALUES ('Lolita', 5, 18);
INSERT INTO books (title, genre_id, author_id) VALUES ('Los Puentes de Madison', 9, 19);
INSERT INTO books (title, genre_id, author_id) VALUES ('Piense y Hágase Rico', 7, 20);
INSERT INTO books (title, genre_id, author_id) VALUES ('Sueño en el Pabellón Rojo', 5, 21);
INSERT INTO books (title, genre_id, author_id) VALUES ('Usted Puede Sanar Su Vida', 7, 22);
INSERT INTO books (title, genre_id, author_id) VALUES ('Veinte Mil Leguas de Viaje Submarino', 5, 23);

INSERT INTO copies (book_id) VALUES (1);
INSERT INTO copies (book_id) VALUES (1);
INSERT INTO copies (book_id) VALUES (1);
INSERT INTO copies (book_id) VALUES (2);
INSERT INTO copies (book_id) VALUES (2);
INSERT INTO copies (book_id) VALUES (2);
INSERT INTO copies (book_id) VALUES (3);
INSERT INTO copies (book_id) VALUES (3);
INSERT INTO copies (book_id) VALUES (3);
INSERT INTO copies (book_id) VALUES (4);
INSERT INTO copies (book_id) VALUES (4);
INSERT INTO copies (book_id) VALUES (4);
INSERT INTO copies (book_id) VALUES (5);
INSERT INTO copies (book_id) VALUES (5);
INSERT INTO copies (book_id) VALUES (5);
INSERT INTO copies (book_id) VALUES (6);
INSERT INTO copies (book_id) VALUES (6);
INSERT INTO copies (book_id) VALUES (6);
INSERT INTO copies (book_id) VALUES (7);
INSERT INTO copies (book_id) VALUES (7);
INSERT INTO copies (book_id) VALUES (7);
INSERT INTO copies (book_id) VALUES (8);
INSERT INTO copies (book_id) VALUES (8);
INSERT INTO copies (book_id) VALUES (8);
INSERT INTO copies (book_id) VALUES (9);
INSERT INTO copies (book_id) VALUES (9);
INSERT INTO copies (book_id) VALUES (9);
INSERT INTO copies (book_id) VALUES (10);
INSERT INTO copies (book_id) VALUES (10);
INSERT INTO copies (book_id) VALUES (10);
INSERT INTO copies (book_id) VALUES (11);
INSERT INTO copies (book_id) VALUES (11);
INSERT INTO copies (book_id) VALUES (11);
INSERT INTO copies (book_id) VALUES (12);
INSERT INTO copies (book_id) VALUES (12);
INSERT INTO copies (book_id) VALUES (12);
INSERT INTO copies (book_id) VALUES (13);
INSERT INTO copies (book_id) VALUES (13);
INSERT INTO copies (book_id) VALUES (13);
INSERT INTO copies (book_id) VALUES (14);
INSERT INTO copies (book_id) VALUES (14);
INSERT INTO copies (book_id) VALUES (14);
INSERT INTO copies (book_id) VALUES (15);
INSERT INTO copies (book_id) VALUES (15);
INSERT INTO copies (book_id) VALUES (15);
INSERT INTO copies (book_id) VALUES (16);
INSERT INTO copies (book_id) VALUES (16);
INSERT INTO copies (book_id) VALUES (16);
INSERT INTO copies (book_id) VALUES (17);
INSERT INTO copies (book_id) VALUES (17);
INSERT INTO copies (book_id) VALUES (17);
INSERT INTO copies (book_id) VALUES (18);
INSERT INTO copies (book_id) VALUES (18);
INSERT INTO copies (book_id) VALUES (18);
INSERT INTO copies (book_id) VALUES (19);
INSERT INTO copies (book_id) VALUES (19);
INSERT INTO copies (book_id) VALUES (19);
INSERT INTO copies (book_id) VALUES (20);
INSERT INTO copies (book_id) VALUES (20);
INSERT INTO copies (book_id) VALUES (20);
INSERT INTO copies (book_id) VALUES (21);
INSERT INTO copies (book_id) VALUES (21);
INSERT INTO copies (book_id) VALUES (21);
INSERT INTO copies (book_id) VALUES (22);
INSERT INTO copies (book_id) VALUES (22);
INSERT INTO copies (book_id) VALUES (22);
INSERT INTO copies (book_id) VALUES (23);
INSERT INTO copies (book_id) VALUES (23);
INSERT INTO copies (book_id) VALUES (23);
INSERT INTO copies (book_id) VALUES (24);
INSERT INTO copies (book_id) VALUES (24);
INSERT INTO copies (book_id) VALUES (24);
INSERT INTO copies (book_id) VALUES (25);
INSERT INTO copies (book_id) VALUES (25);
INSERT INTO copies (book_id) VALUES (25);
INSERT INTO copies (book_id) VALUES (26);
INSERT INTO copies (book_id) VALUES (26);
INSERT INTO copies (book_id) VALUES (26);
INSERT INTO copies (book_id) VALUES (27);
INSERT INTO copies (book_id) VALUES (27);
INSERT INTO copies (book_id) VALUES (27);
INSERT INTO copies (book_id) VALUES (28);
INSERT INTO copies (book_id) VALUES (28);
INSERT INTO copies (book_id) VALUES (28);
INSERT INTO copies (book_id) VALUES (29);
INSERT INTO copies (book_id) VALUES (29);
INSERT INTO copies (book_id) VALUES (29);
INSERT INTO copies (book_id) VALUES (30);
INSERT INTO copies (book_id) VALUES (30);
INSERT INTO copies (book_id) VALUES (30);
''')