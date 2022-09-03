#Importar librerias
import time
from tqdm import tqdm
from time import sleep
import string
import random
from colorama import Fore, Style


#Declarar variables
alto = 0
ancho = 0
opcionJuego = 0
configurarTamanno = 0
lineasLowerCompu = []
lineasLower = []
palabrasComputadora = []
palabrasPartidaPropia = []
matriz = []
listaRespuestas = []
palabrasOrdenAlfabeto = []
respuestasOrdenAlfabeto = []

######################################
###############FUNCIONES##############
######################################

#####MENU DE BIENVENIDA#####
def menuBienvenida():

    print(Fore.BLUE + "                  ---------                     ")
    time.sleep(0.2)
    print("            ---------------------               ")
    time.sleep(0.2)
    print("      ---------------------------------         ")
    time.sleep(0.2)
    print("---------------------------------------------   ")
    time.sleep(0.2)
    print("                  ---------                     ")
    time.sleep(0.2)
    print("            ---------------------               ")
    time.sleep(0.2)
    print("      ---------------------------------         ")
    time.sleep(0.2)
    print("---------------------------------------------   " + Style.RESET_ALL)
    time.sleep(0.2)
    print("                                                ")
    print(Fore.GREEN + "                SOPA DE LETRAS                  " + Style.RESET_ALL)
    time.sleep(0.2)
    print("                                                ")
    print(Fore.BLUE + "---------------------------------------------   ")
    time.sleep(0.2)
    print("      ---------------------------------         ")
    time.sleep(0.2)
    print("            ---------------------               ")
    time.sleep(0.2)
    print("                  ---------                     ")
    time.sleep(0.2)
    print("---------------------------------------------   ")
    time.sleep(0.2)
    print("      ---------------------------------         ")
    time.sleep(0.2)
    print("            ---------------------               ")
    time.sleep(0.2)
    print("                  ---------                     ")
    time.sleep(0.2)
    print("                      -")
    time.sleep(0.2)
    print("                      -")
    time.sleep(0.2)
    print("                      -" + Style.RESET_ALL)
    time.sleep(0.2)


#####MENU DE OPCIONES DE JUEGO#####
def opcionesMenu():
    for i in tqdm(range(100)):
         sleep(0.02)
    print(Fore.GREEN + "-------------------------------------------------")
    time.sleep(0.2)
    print("---             OPCIONES DE JUEGO             ---")
    time.sleep(0.2)
    print("-------------------------------------------------")
    time.sleep(0.2)
    print("Para iniciar un juego nuevo ingrese '1'.")
    time.sleep(0.2)
    print("Para configurar su propia partida ingrese '2'.")
    time.sleep(0.2)
    print("Para cerrar esta sesión ingrese '3'.")
    time.sleep(0.2)
    
    opcionJuego = int(input("---------> " + Style.RESET_ALL))
    return opcionJuego


#####LEER DOC .TXT PARA PARTIDA COMPUTADORA / Convertir a minúscula#####
def leerPalabrasComputadora(filename='palabrasComputadora.txt'):
    lineas = []
    with open(filename) as archivo:
        for linea in archivo.readlines():
            lineas.append(linea)
        lineas = [x[:-1] for x in lineas]
        for i in lineas:
            i = i.lower()
            lineasLowerCompu.append(i)
        return lineasLowerCompu


#####LEER DOC .TXT PARA PARTIDA PROGRAMADA POR USUARIO / Convertir a minúscula#####
def leerPalabrasPartidaPropia(filename='palabras.txt'):
    lineas = []
    with open(filename) as archivo:
        for linea in archivo.readlines():
            lineas.append(linea)
        lineas = [x[:-1] for x in lineas]
        for i in lineas:
            i = i.lower()
            lineasLower.append(i)
        return lineasLower


#####IMPRIMIR LISTA VERTICAL#####
def listaVertical(lista):
    for i in lista:
        print(Fore.GREEN + i  + Style.RESET_ALL)


#####SOLICITAR TAMAÑO DE MATRIZ PARTIDA PROPIA#####
def configurarPartida(configurarTamanno):
    print(Fore.GREEN + "-------------------------------------------------")
    print("---        CONFIGURE SU PROPIA PARTIDA        ---")
    print("-------------------------------------------------")
    print("Indique el tamaño de matriz que desea (ingrese el número correspondiente): ")
    print("1. Matriz 10 x 10")
    print("2. Matriz 15 x 15")
    print("3. Matriz 20 x 20")
    configurarTamanno = int(input("----------> " + Style.RESET_ALL))
    return configurarTamanno


#####MUESTRA INSTRUCCIONES DE LLENADO DE PALABRAS PARA LA PARTIDA PROPIA, Y CONFIRMACIÓN DE LLENADO#####
def indicarLlenadoExitoso(configurarPartida):
    cantidadPalabras = 0
    if(configurarPartida == 1):
        cantidadPalabras = 5
    elif(configurarPartida == 2):
        cantidadPalabras = 8
    else:
        cantidadPalabras = 10
    print(Fore.RED + f"Por favor ingrese {str(cantidadPalabras)} palabras al archivo 'palabras.txt'.")
    print("Pro tip: no olvide guardar el documento.")
    indicarLlenadoExitoso = input("Inserte '1' cuando haya completado las instrucciones anteriores: " + Style.RESET_ALL)
    if(indicarLlenadoExitoso == 1):
        return configurarTamanno
    else:
        pass


#####DETERMINAR ALTO Y ANCHO#####
def determinarAltoAncho(configurarTamanno, alto, ancho):
    if(configurarTamanno == 1):
        alto = 10
        ancho = 10
    elif(configurarTamanno == 2):
        alto = 15
        ancho = 15
    elif(configurarTamanno == 3):
        alto = 20
        ancho = 20
    else:
        alto = 15
        ancho = 15
    return alto, ancho


#####INPUT DE RESPUESTAS#####
def ingresarRespuestas(palabras, listaRespuestas):
    continuar = True
    while continuar == True:
        respuesta = input(Fore.YELLOW + "Ingrese palabras encontradas aquí (una a la vez): " + Style.RESET_ALL)
        respuesta = respuesta.lower()
        if(respuesta in palabras):
            print(Fore.GREEN + f"Ha encontrado la palabra '{respuesta.upper()}'!" + Style.RESET_ALL)
            listaRespuestas.append(respuesta)
            siguiente = input(Fore.YELLOW + "Desea seguir? (si / no)? " + Style.RESET_ALL)
            siguiente.lower()
            if(siguiente == 'no'):
                continuar = False
            else:
                continuar = True
        else:
            print(Fore.RED + "Esta palabra no existe en la sopa." + Style.RESET_ALL)
            siguiente = input(Fore.YELLOW + "Desea seguir? (si / no)? " + Style.RESET_ALL)
            siguiente.lower()
            if(siguiente == 'no'):
                continuar = False
            else:
                continuar = True
    palabras.sort()
    palabrasOrdenAlfabeto = palabras
    listaRespuestas.sort()
    respuestasOrdenAlfabeto = listaRespuestas
    return palabrasOrdenAlfabeto, respuestasOrdenAlfabeto


#####IMPRESIÓN DE PALABRAS ENCONTRADAS Y NO ENCONTRADAS AL FINALIZAR UNA SESIÓN#####
def palabrasEncontradas(palabrasOrdenAlfabeto, respuestasOrdenAlfabeto):
    if(palabrasOrdenAlfabeto != respuestasOrdenAlfabeto):
        print(Fore.GREEN + "----------------------------------------------")
        if(len(respuestasOrdenAlfabeto) == 1):
            print("Ha logrado encontrar la siguiente palabra: " + Style.RESET_ALL)
        elif(len(respuestasOrdenAlfabeto) > 1):
            print("Ha logrado encontrar las siguientes palabras: " + Style.RESET_ALL)
        else:
            pass

        for palabra in palabrasOrdenAlfabeto:
            if palabra in respuestasOrdenAlfabeto:
                print(Fore.GREEN + f"---> {palabra.upper()}" + Style.RESET_ALL)
            else:
                pass
        if((len(palabrasOrdenAlfabeto)) - (len(respuestasOrdenAlfabeto)) == 1):
            print(Fore.RED + "No logró encontrar la siguiente palabra: " + Style.RESET_ALL)
        elif((len(palabrasOrdenAlfabeto)) - (len(respuestasOrdenAlfabeto)) > 1):
            print(Fore.RED + "No logró encontrar las siguientes palabras: " + Style.RESET_ALL)
        else:
            pass

        for palabra in palabrasOrdenAlfabeto:
            if palabra in respuestasOrdenAlfabeto:
                pass
            else:
                print(Fore.RED + f"---> {palabra.upper()}" + Style.RESET_ALL)
        
    else:
        print(Fore.GREEN + "----------------------------------------------------")
        print("---   Ha logrado encontrar todas las palabras!   ---")   
        print("----------------------------------------------------" + Style.RESET_ALL)

    pass


#####REVISAR RESPUESTAS E IMPRIMIR SI GANÓ O NO
def revisarRespuestas(palabrasOrdenAlfabeto, respuestasOrdenAlfabeto):
    if(palabrasOrdenAlfabeto == respuestasOrdenAlfabeto):
        print(Fore.GREEN + "   ***   ***   ***   ***   ***   ***   ***   ***")
        time.sleep(0.1)
        print("   ***   ***   ***               ***   ***   ***")
        time.sleep(0.1)
        print("   ***   ***           ---             ***   ***")
        time.sleep(0.1)
        print("   ***              HA GANADO!               ***")
        time.sleep(0.1)
        print("   ***   ***           ---             ***   ***")
        time.sleep(0.1)
        print("   ***   ***   ***               ***   ***   ***")
        time.sleep(0.1)
        print("   ***   ***   ***   ***   ***   ***   ***   ***" + Style.RESET_ALL)
    else:
        print(Fore.RED +"***   ***   ***   ***   ***   ***   ***   ***   ***   ***")
        time.sleep(0.1)
        print("***                                                             ***")
        time.sleep(0.1)
        print("***                   Inténtelo de nuevo!                       ***")
        time.sleep(0.1)
        print("***                                                             ***")
        time.sleep(0.1)
        print("***   ***   ***   ***   ***   ***   ***   ***   ***   ***" + Style.RESET_ALL)


#####CERRAR SESIÓN#####
def cerrarSesion():
    print(Fore.RED + "--------------------------------------------------")
    print("---         Ha abandonado esta sesión.         ---")
    print("--------------------------------------------------" + Style.RESET_ALL)


