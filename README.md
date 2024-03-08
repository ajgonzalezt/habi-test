# habi-test
Para este proyecto, implementaré un servicio REST sin utilizar ningún framework. Utilizaré una base de datos MySQL para acceder a los datos que necesito consultar. Para crear los endpoints de la API, usaré la biblioteca BaseHTTPRequestHandler. También realizaré pruebas con unittest para verificar que las respuestas de la API sean correctas.

Para organizar el código, seguiré un estilo de arquitectura MVC (Modelo, Vista, Controlador). Esto me ayudará a mantener el código ordenado y a dividir las responsabilidades de manera clara, lo que facilitará su lectura y mantenimiento.


Para el segundo punto del primer ejercicio, el requerimiento que hace posible  a un usuario dar like a una propiedad, se propone el siguiente modelo:


![UML_for_likes](https://github.com/ajgonzalezt/habi-test/assets/47196362/f8f3a450-d4c2-4429-846b-9db6073c0b2d)


Como se puede ver en la imagen, se decidio añadir a las tablas ya existentes, una tercera tabla que modele la relacion entre los usuarios y las propiedad, esta tabla tendra entonces la llave foranea a la propiedad y la llave foranea al usuarii autenticado, ademas de tambien almacenar la fecha de cada uno de los likes a las propiedades.

Decidi hacerlo de esta manera ya que asi se puede almacenar la relacion de todos los usuarios con todas las propiedades a las cuales se dio like, sin perder ninguna informacion y permitiendo un acceso facil, adicionalmente de esta manera se pude llevar registro de en que fecha se le dio like, lo que puede generar ciertas ventajas al negocio y poder estudiar mejor el como interactuan los usuarios con las propiedades

y la sentencia necesaria para crear esta tabla es:

CREATE TABLE likes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_user INT,
    id_property INT,
    updated_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (id_user) REFERENCES aut_user(id),
    FOREIGN KEY (id_property) REFERENCES properties(id)
);
