## gestión de videoclub version 2020
def añadirPelicula(listaPeliculas):
    cantidad=int(input("dame la cantidad de copias que quieres introducir: "))
    global contadorPeliculas #con global estamos indicando que contadorPeliculas
    global idPelicula        #es la variable declarada en el programa principal
    
    if (contadorPeliculas + cantidad <=MAX_PELICULAS):#si queda hueco para añadir las
                                 #nuevas peliculas la añado
        pelicula=dict()
        contadorPeliculas+=cantidad
        idPelicula+=1
        pelicula[0]=idPelicula
        pelicula[1]=input("dame el título de la peli: ")
        pelicula[2]=input("dame el director de la peli: ")
        pelicula[3]=input("dame el género de la peli: ")
        pelicula[4]=input("dame el año de la peli: ")           
        pelicula[5]=input("dame la duración en minutos: ")
        pelicula[6]=True    #por defecto, inicialmente está disponible
        pelicula[7]=cantidad 
        pelicula[8]=0 #por defecto, inicialmente no hay ninguna pelicula reservada
        listaPeliculas.append(pelicula)
    else:
        print ("No hay sitio para almacenar %d películas, ya que solo hay hueco\
para %d películas más." % (cantidad,(MAX_PELICULAS-contadorPeliculas)))
    return listaPeliculas #no es necesario realizar este return, pero nos lo piden

def reservarPelicula():
    global listaPeliculas
    listarPeliculas()
    id_peli=int(input("dame el id de la película que quieres reservar"))
    salir=False
    if (id_peli<=idPelicula and id_peli>0):
        if listaPeliculas[id_peli-1][6]==True:
            print ("la película ha sido reservada")
            listaPeliculas[id_peli-1][7]-=1 #tal y como solicita el enunciado la primera peli
            if listaPeliculas[id_peli-1][7]==0: # tiene id 1, pero su posición es la 0, por tanto,
                listaPeliculas[id_peli-1][6]=False # si quiere acceder a la pelicula con id 5,
                                                    # su posición es 0
        else:
            print ("lo sentimos, la película que quieres reservar no está \
disponible")
    else:
        print ("El id de la película no existe en este videoclub")
        
def listarPeliculas():
    global listaPeliculas
    print ("===============================")
    print ("listado de películas")
    print ("===============================")    
    for i in listaPeliculas:#listaPeliculas es la lista que forma parte del programa principal
        mostrarPelicula(i) #¿y por qué no usamos global? La respuesta es que solo la estamos consultando
                            #python lo interpreta de esta manera: ¿listaPeliculas existe en este
                            # procedimiento y además no le estoy asignando algo p.ej: listaPeliculas=0
                            # si hicieramos eso, crearía una nueva variable local dentro de la función
                            # leed atentamente el artículo que publiqué en el classroom
def mostrarPelicula(peli):
        if peli[6]==True:
            disponible="Disponible" # almaceno en esta variable el literal "disponible"
        else:
            disponible="No disponible"
        print ("Id: %d Título: %s Director:%s Género: %s \
Año: %s Duración: %s minutos Estado: %s"%(peli[0],peli[1],peli[2],peli[3],\
                                          peli[4],peli[5],disponible))



def buscarPelicula():
    opcion=menu_buscar()
    texto=input("Introduce el texto que quieres que aparezca en la búsqueda:\
")
    mostradas=0
    for i in listaPeliculas:
        if texto in i[opcion]:
            mostrarPelicula(i)
            mostradas+=1
    if mostradas ==0:
        print ("No existe ningún título que cumpla con los criterios de búsqued\
a seleccionados")
                
def menu_buscar():
    print ("¿Qué tipo de búsqueda deseas realizar?")
    print ("1) por título")
    print ("2) por director")
    print ("3) por género")
    print ("4) por año")
    print ("5) por duracion ")
    return int(input())              

def mostrarMenu():
    global listaPeliculas
    salir=False
    while salir==False:
        print ("=========================")
        print ("=   M   E   N   Ú       =")
        print ("=========================")
        print (" 1) añadir película  ")
        print (" 2) reservar película ")
        print (" 3) buscar películas ")
        print (" 4) salir")               
        print ("=========================")           
        opcion=int(input("¿Qué opción deseas? "))
        if opcion==1:
            listaPeliculas=añadirPelicula(listaPeliculas)
        elif opcion==2:
            reservarPelicula()
        elif opcion==3:
            buscarPelicula()
        elif opcion==4:
            salir=True
        else:
            print ("LA OPCION INTRODUCIDA ES INCORRECTA, VUELVA A INTENTARLO ")

# =================== PROGRAMA PRINCIPAL ============================
#La informacion la guardaremos en forma de lista de diccionarios.
listaPeliculas=[]

# CONSTANTES
MAX_PELICULAS=3000

#VARIABLES
contadorPeliculas=0
idPelicula=0

#inicio de programa
mostrarMenu()
