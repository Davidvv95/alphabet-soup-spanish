#Importar archivos python
from funciones import *

if __name__ == '__main__':
    #Menu de bienvenida
    menuBienvenida()
    #Menu de opciones (escoger entre jugar con un juego pre-configurado, configurar su propio juego, o cerrar sesión)
    inicializar = opcionesMenu()

    #####JUEGO NUEVO#####
    if(inicializar == 1):
        #Determinar dimensiones de la matriz
        alto = 10
        ancho = 10

        #Leer archivo .txt de juego preconfigurado y convertir las palabras a minúscula
        palabrasComputadora = leerPalabrasComputadora(filename='palabrasComputadora.txt')
        #Imprimir lista vertical de palabras que se deben encontrar
        listaVertical(palabrasComputadora)



 
        #CREAR MATRIZ
        matriz = [[random.choice(string.ascii_lowercase) for i in range(0, ancho)] for j in range(0, alto)] #Llenar matriz con letras aleatoriamente
        for palabra in palabrasComputadora:
            #Matriz X
            direccion = random.choice([[1,0],[0,1],[1,1]]) # Determinar dirección de la palabra: 1,0 es derecha, 0,1 es izquierda, 1,1 es diagonal
            if(direccion[0] == 0): #Evita que palabras se salgan de la matriz horizontalmente
                tamannoPalabraX = ancho
            else:
                tamannoPalabraX = ancho - len(palabra)
            #Matrix Y
            if(direccion[1] == 0): #Evita que palabras se salgan de la matriz verticalmente
                tamannoPalabraY = alto
            else:
                tamannoPalabraY = alto - len(palabra)
            x = random.randrange(0, tamannoPalabraX)
            y = random.randrange(0, tamannoPalabraY)
            
            #Loop que coloca las palabras dentro de la matriz en posición y dirección aleatoria
            for i in range(0, len(palabra)):
                matriz[y + direccion[1] * i][x + direccion[0] * i] = palabra[i]
            palabra = random.choice([palabra, palabra[::-1]])
        #Imprimir la matriz
        print (Fore.GREEN + "\n".join(map(lambda row: " ".join(row), matriz)) + Style.RESET_ALL)



        #Pedir al usuario que ingrese palabras encontradas. Estas se acumulan en una lista 
        #Ambas listas se reordenan en orden alfabético para ser comparadas
        palabrasOrdenAlfabeto, respuestasOrdenAlfabeto = ingresarRespuestas(palabrasComputadora, listaRespuestas)
        #Imprimir palabras encontradas y no encontradas
        palabrasEncontradas(palabrasOrdenAlfabeto, respuestasOrdenAlfabeto)
        #Se revisan las respuestas del usuario, comparando respuestas con la lista original de palabras
        # Con base en esto se imprime un mensaje: ganó o no ganó?
        revisarRespuestas(palabrasOrdenAlfabeto, respuestasOrdenAlfabeto)



    
    #####JUEGO CONFIGURADO#####
    elif(inicializar == 2):
        #Menú para escoger tamaño de matriz (10x10, 15x15 o 20x20)
        configurarPartida = configurarPartida(configurarTamanno)
        #Pedir al usuario que llene el archivo .txt con las palabras deseadas y las guarde
        indicarLlenadoExitoso(configurarPartida)
        #Leer archivo .txt con palabras ingresadas por el usuario. Convierte las palabras a minúscula
        palabrasPartidaPropia = leerPalabrasPartidaPropia(filename='palabras.txt')
        #Determina las dimensiones de la matriz, según indicó el usuario con la función configurarPartida
        alto, ancho = determinarAltoAncho(configurarPartida, alto, ancho)
        #Imprimir lista vertical de palabras que se deben encontrar
        listaVertical(palabrasPartidaPropia)




        #CREAR MATRIZ
        matriz = [[random.choice(string.ascii_lowercase) for i in range(0, ancho)] for j in range(0, alto)] #Llenar matriz con letras aleatoriamente
        for palabra in palabrasPartidaPropia:
            #Matriz X
            direccion = random.choice([[1,0],[0,1],[1,1]]) # Determinar dirección de la palabra: 1,0 es derecha, 0,1 es izquierda, 1,1 es diagonal
            if(direccion[0] == 0): #Evita que palabras se salgan de la matriz horizontalmente
                tamannoPalabraX = ancho
            else:
                tamannoPalabraX = ancho - len(palabra)
            #Matrix Y
            if(direccion[1] == 0): #Evita que palabras se salgan de la matriz verticalmente
                tamannoPalabraY = alto
            else:
                tamannoPalabraY = alto - len(palabra)
            x = random.randrange(0, tamannoPalabraX)
            y = random.randrange(0, tamannoPalabraY)
            
            #Loop que coloca las palabras dentro de la matriz en posición y dirección aleatoria
            for i in range(0, len(palabra)):
                matriz[y + direccion[1] * i][x + direccion[0] * i] = palabra[i]
            palabra = random.choice([palabra, palabra[::-1]])
        #Imprimir la matriz
        print (Fore.GREEN + "\n".join(map(lambda row: " ".join(row), matriz)) + Style.RESET_ALL)



        #Pedir al usuario que ingrese palabras encontradas. Estas se acumulan en una lista 
        #Ambas listas se reordenan en orden alfabético para ser comparadas
        palabrasOrdenAlfabeto, respuestasOrdenAlfabeto = ingresarRespuestas(palabrasPartidaPropia, listaRespuestas)
        #Imprimir palabras encontradas y no encontradas
        palabrasEncontradas(palabrasOrdenAlfabeto, respuestasOrdenAlfabeto)
        #Se revisan las respuestas del usuario, comparando respuestas con la lista original de palabras
        # Con base en esto se imprime un mensaje: ganó o no ganó?
        revisarRespuestas(palabrasOrdenAlfabeto, respuestasOrdenAlfabeto)

            


    else:
        cerrarSesion()


