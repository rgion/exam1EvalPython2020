# exam1EvalPython2020

<table>
  <tr>
   <td><strong>Nombre y apellidos:</strong>
   </td>
   <td>
   </td>
   <td><strong>Fecha:</strong>
   </td>
   <td><strong>2/12/2020</strong>
   </td>
  </tr>
  <tr>
   <td><strong>Módulo</strong>
   </td>
   <td>Seguridad y alta disponibilidad
   </td>
   <td><strong>CFGS</strong>
   </td>
   <td><strong>ASIX</strong>
   </td>
  </tr>
</table>


**<span style="text-decoration:underline;">Normativa:</span>** 



1. El examen se debe resolver con los conceptos vistos en clase: funciones, procedimientos, if, else, elif for, while, listas, diccionarios, cadenas…
2. Se pueden realizar más funciones de las indicadas.
3. **<span style="text-decoration:underline;">No se puede abrir el navegador</span>**, así como cualquier tipo de software de comunicación. El incumplimiento de esta norma es motivo de finalización del examen, y por tanto, no será corregido.
4. **Se pueden consultar los <span style="text-decoration:underline;">pdf</span> del aula virtual** <span style="text-decoration:underline;">mediante un lector de pdf</span> (excluido el navegador), así como los programas realizados durante las prácticas.
5. **Nada más iniciar el examen lo primero** que debéis incluir es una cabecera que aparezca:     #nombre apellido apellido2 – examen 1º DAM
6. Al finalizar se debe realizar commit y push. Comprobamos a continuación si efectivamente está en el repositorio. 
7. **Solo se debe realizar commit o push cuando lo indique el profesor.**

**<span style="text-decoration:underline;">Criterio de evaluación:</span>** Cada apartado en el que aparezca la puntuación se evaluará de la siguiente manera:



*   La puntuación se ha asignado a cada uno de los apartados.
*   1 punto por la calidad general del código: nombrado de variables, estructuras de datos, funciones, procedimientos, comentarios en el código, etc.
1. **<span style="text-decoration:underline;">Gestión de videoclub</span>**

Una empresa que gestiona un videoclub de Palma, nos ha solicitado el desarrollo de un programa de gestión. Tras recabar los requisitos, el analista nos ha pedido que hagamos lo siguiente:



1. El **programa principal** **(0,5 punto)** tendrá un menú que se llamará indefinidamente hasta que el usuario quiera salir de la aplicación. En el menú, entre otras cosas llamará a las funciones/procedimientos que se detallan a continuación. 
2. Función **añadirPelículas**  **(2,5 puntos)**, se encargará de realizar el alta de una película, en la que se solicitará la siguiente información: <span style="text-decoration:underline;">id, título, director, duración, género, duración, año, disponible (cierto=disponible, falso=no disponible), cantidad de copias total, cantidad de copias reservadas).</span> La función se caracteriza por:
    *   Tener como parámetro la lista de películas del videoclub, y al finalizar devolverá la lista actualizada con la nueva película incluida. 
    *   Además, hay que tener en cuenta que el videoclub, solo podrá almacenar en total 3000 copias de películas, por tanto, si se quiere añadir alguna copia más, mostrará un mensaje de error “el videoclub no puede almacenar más copias”, y no permitirá añadir la película.
    *   A cada nuevo título se le asignará un id secuencial que empezará en 1, y que será único para cada título.
    *   Al dar de alta la película no habrá ninguna película reservada.
3. El procedimiento **reservarPelícula(2 puntos)**, <span style="text-decoration:underline;">no recibirá como parámetro ningún argumento</span> de manera que lo primero que hará será llamar al procedimiento **listar_peliculas**. En este procedimiento hay que tener en cuenta:
    *   Una vez listada las películas, se pedirá al usuario el <span style="text-decoration:underline;">id</span> del título de la película que quiere reservar. 
    *   Si no hay películas disponibles, es decir, <span style="text-decoration:underline;">disponible</span> = falso, mostraremos un mensaje de aviso que no está disponible la película. 
    *   Si hay películas disponibles, enviaremos un mensaje informativo de que ha sido reservada, actualizaremos la <span style="text-decoration:underline;">cantidad de copias reservadas</span>, y si estas fueran igual a la <span style="text-decoration:underline;">cantidad de copias total</span>, actualizaremos <span style="text-decoration:underline;">disponible</span> a falso. 
    *   Si introducimos un número que no se corresponde con ningún id, mostrará un mensaje informando que el número introducido no es correcto.
4. El procedimiento **listarPeliculas (1 punto)** no recibirá como parámetro ningún argumento y mostrará la información de todos los títulos: <span style="text-decoration:underline;">id, título, director, género, duración y el estado (disponible o no disponible)</span>.
5. El procedimiento **buscarPeliculas (4 puntos)** que no recibirá como parámetro ningún argumento, preguntará al usuario que tipo de búsqueda quiere hacer por <span style="text-decoration:underline;">título, director, género, duración o año</span>, de manera que la búsqueda esté parametrizada (cuando hablamos de parametrizada estamos hablando de tratar de hacer una búsqueda que sea común y única para cualquier búsqueda, ya sea título, director, género, año, etc). Además, esta búsqueda mostrará todos aquellos títulos que **incluyan el texto de búsqueda (parte o completamente)** , y si fuera el caso de no encontrar ninguna película que cumpla con los criterios de búsqueda, mostrará un mensaje informando que no ha encontrado nada.

    **Muestra de ejecución:**


    ```
    =========================
    =   M   E   N   Ú       =
    =========================
     1) añadir película  
     2) reservar película 
     3) buscar películas 
     4) salir
    =========================
    ¿Qué opción deseas? 1
    dame la cantidad de copias que quieres introducir: 2
    dame el título de la peli: El padrino I
    dame el director de la peli: Francis Ford Coppola
    dame el género de la peli: Drama
    dame el año de la peli: 1972
    dame la duración en minutos: 180
    =========================
    =   M   E   N   Ú       =
    =========================
     1) añadir película  
     2) reservar película 
     3) buscar películas 
     4) salir
    =========================
    ¿Qué opción deseas? 1
    dame la cantidad de copias que quieres introducir: 1
    dame el título de la peli: El padrino II
    dame el director de la peli: Francis Ford Coppola
    dame el género de la peli: Drama
    dame el año de la peli: 1974
    dame la duración en minutos: 190
    =========================
    =   M   E   N   Ú       =
    =========================
     1) añadir película  
     2) reservar película 
     3) buscar películas 
     4) salir
    =========================
    ¿Qué opción deseas? 2
    ===============================
    Listado de películas
    ===============================
    Id: 1 Título: El padrino I Director: Francis Ford Coppola Género: Drama Año: 1972 Duración: 180 minutos Estado: Disponible
    Id: 2 Título: El padrino II Director: Francis Ford Coppola Género: Drama Año: 1974 Duración: 190 minutos Estado: Disponible
    Dame el id de la película que quieres reservar5
    El id de la película no existe en este videoclub
    =========================
    =   M   E   N   Ú       =
    =========================
     1) añadir película  
     2) reservar película 
     3) buscar películas 
     4) salir
    =========================
    ¿Qué opción deseas? 2
    ===============================
    Listado de películas
    ===============================
    Id: 1 Título: El padrino I Director: Francis Ford Coppola Género: Drama Año: 1972 Duración: 180 minutos Estado: Disponible
    Id: 2 Título: El padrino II Director: Francis Ford Coppola Género: Drama Año: 1974 Duración: 190 minutos Estado: Disponible
    Dame el id de la película que quieres reservar2
    La película ha sido reservada
    =========================
    =   M   E   N   Ú       =
    =========================
     1) añadir película  
     2) reservar película 
     3) buscar películas 
     4) salir
    =========================
    ¿Qué opción deseas? 2
    ===============================
    Listado de películas
    ===============================
    Id: 1 Título: El padrino I Director: Francis Ford Coppola Género: Drama Año: 1972 Duración: 180 minutos Estado: Disponible
    Id: 2 Título: El padrino II Director: Francis Ford Coppola Género: Drama Año: 1974 Duración: 190 minutos Estado: No disponible
    Dame el id de la película que quieres reservar1
    La película ha sido reservada
    =========================
    =   M   E   N   Ú       =
    =========================
     1) añadir película  
     2) reservar película 
     3) buscar películas 
     4) salir
    =========================
    ¿Qué opción deseas? 3
    ¿Qué tipo de búsqueda deseas realizar?
    1) por título
    2) por director
    3) por género
    4) por año
    5) por duración 
    1
    Introduce el texto que quieres que aparezca en la búsqueda: padri
    Id: 1 Título: El padrino I Director: Francis Ford Coppola Género: Drama Año: 1972 Duración: 180 minutos Estado: Disponible
    Id: 2 Título: El padrino II Director: Francis Ford Coppola Género: Drama Año: 1974 Duración: 190 minutos Estado: No disponible
    =========================
    =   M   E   N   Ú       =
    =========================
     1) añadir película  
     2) reservar película 
     3) buscar películas 
     4) salir
    =========================
    ¿Qué opción deseas? 3
    ¿Qué tipo de búsqueda deseas realizar?
    1) por título
    2) por director
    3) por género
    4) por año
    5) por duración 
    1
    Introduce el texto que quieres que aparezca en la búsqueda: otro padrino
    No existe ningún título que cumpla con los criterios de búsqueda seleccionados
    =========================
    =   M   E   N   Ú       =
    =========================
     1) añadir película  
     2) reservar película 
     3) buscar películas 
     4) salir
    =========================
    ¿Qué opción deseas? 4
