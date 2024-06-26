"""
Una biblioteca necesita desarrollar una aplicación que permita gestionar el préstamo de libros y calcular el total de
libros prestados por cada usuario. La aplicación debe cumplir con las siguientes funcionalidades:
1. Registrar libro
2. Prestar libro
3. Listar todos los libros
4. Imprimir reporte de préstamos
5. Salir del Programa
Cada una de estas opciones de la aplicación debe estar desarrollada en una función que debe ser llamada desde el
programa principal.
Registrar libro
Para registrar un libro se requiere los siguientes datos: Título, Autor, Año de Publicación, SKU. Debe validar que
todos los datos sean ingresados.
Nota: El SKU es el identificador único de cada libro, facilitando su búsqueda y adquisición en librerías y bibliotecas.
Ejemplo de SKU es las 6 primeras letras del título del libro – las 3 primeras letras del autor – año de publicación.
Prestar libro
Para prestar un libro se requiere: Nombre del usuario y SKU del libro. Debe validar que el libro exista y que no esté
ya prestado.
Listar todos los libros
Debe mostrar en la pantalla la lista de todos los libros registrados.
TÍTULO AUTOR AÑO DE PUBLICACIÓN SKU


"""
libros=[
    ["Título  ","Autor           ","Año ", "SKU          "],
    ["ejemplo1","anonimo apellido","2024","ejemplo1anonimo2024"]
]

prestados=[
    ["Nombre usuario","Título", "SKU", "fecha"],
    ["ejemplo1","anonimo","ejemplo1anonimo2024","05-01-2023"]
]

def Registrar_libro():
    while True:
        try:
            "*** REGISTRO LIBROS ***"
            print("ingrese los datos del libro a Registrar")
            titulo=input("Titulo:\t").lower()
            nombre=input("Nombre Autor:\t").lower()
            apellido=input("Apellido Autor:\t").lower()
            anno=int(input("Año de Publicación:\t"))
            #VALIDAR DATOS
            while titulo=="" or nombre=="" or apellido=="" or anno=="":
                try:
                    if titulo=="":
                        print("Debe ingresar titulo del libro")
                        titulo=input("Titulo:\t")

                    elif nombre=="":
                        print("Debe ingresar el Nombre Autor")
                        nombre=input("Nombre Autor:\t")

                    elif apellido=="":
                        print("Debe ingresar el Apellido Autor")
                        apellido=input("Apellido Autor:\t")
                    elif anno=="":
                        print("Debe ingresar el Año de Publicación")
                        anno=int(input("Año de Publicación:\t"))
                    else:
                        break
                except:
                    print("opción no valida")

            sku=titulo+str(anno)
            sku=(str(sku)).strip()

            libros.append([titulo,(nombre+" "+apellido),anno,sku])

            resp=input("¿desea agregar otro libro? s/n")
            if resp.lower()!="s":
                break
        except:
            print("error vuelva a intentar")



def Prestar_libro():
    while True:
        try:
            print("*** PRESTAMOS ***")
            usuario=input("Ingrese nombre usuario  que desea prestamo:\t")
            sku=input ("Ingrese codigo SKU del libro:\t")
            titulo=""
            existe=False
            Notprestado=True
            #validación

            for linea in libros :

                if (linea[3].strip()).lower() == (sku.strip()).lower():
                    titulo=linea[0]
                    existe =True

            for linea in prestados:
                if (linea[2].strip()).lower()==(sku.strip()).lower():
                        Notprestado=False
            
            if existe==True and Notprestado==True:
                print("Libro disponible ")
                fecha=input("ingrese la fecha de prestamo formato DD/MM/AAAA:\t")
                if fecha!="":
                    prestados.append([usuario,titulo, sku, fecha])
                    print("se ha registrado de forma correcta el prestamo\t")
                else:
                    print("fecha no ingresada")
            elif Notprestado==False and existe==True:
                print("el libro no se encuentra disponible")
            else :
                print("el libro no existe")

            resp=input("¿desea otro prestamo? s/n\t")
            if resp.lower()!="s":
                break
            

        except:
            print("datos no validos")


def Listar_libros():
    print("*** LIBROS ***")

    #contenido
    for libro in libros:
        print(f"{libro[0]}\t{libro[1]}\t{libro[2]}\t{libro[3]}")



def Imprimir_préstamos():
    with open ("prestamos.txt","w")as archivo_txt:
        for linea in libros:
            archivo_txt.write(linea[0]+"'\t"+linea[1]+"\t"+linea[3]+"\n")
    
    print("archivo creado exitosamente")


    


def menu():
    while True:
        try:
            print("**** MENU BIBLIOTECA ****")
            op=int(input("1. Registrar libro\n2. Prestar libro\n3. Listar todos los libros\n4. Imprimir reporte de préstamos\n5. Salir del Programa\n"))

            if   op == 1:
                Registrar_libro()
            elif op == 2:
                Prestar_libro()
            elif op == 3:
                Listar_libros()
            elif op == 4:
                Imprimir_préstamos()
            elif op == 5:
                print(" Programa finalizado…\nDesarrollado por Tiare Pérez\nRUN: 19.551.177-2 ")
                break
        except:
            print("opción no validad reintente")











