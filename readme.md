INF-05 Principios de Programación 
TC16

Estudiantes:
David van Veen
Daniela Aguilar Murillo
Kevin Jiménez Mendoza

Profesor: 
Keylor JesúS Guevara Jiménez

PROYECTO FINAL - SOPA DE LETRAS

PREPARAR AMBIENTE
1. Instalar python

2. Idealmente utilizar Visual Studio Code.
Instalar la siguiente extensión de ser necesario:
- Python (Intellisense)

3. Se requiere los siguientes archivos dentro de la misma carpeta:
- funciones.py
- main.py
- palabras.txt
- palabrasComputadora.txt

4. Posiblemente sea necesario instalar algunas librerías:
- tqdm
- colorama
Usar el comando:
'pip install tqdm'
Este comando instala ambos (colorama y tqdm).
De no ser así, correr también el comando:
'pip install colorama'


SOPA DE LETRAS
Se trata del popular juego que consiste en encontrar palabras dentro de una matriz cuadrada, llena de letras aleatorias que esconden las palabras por buscar.

CÓMO FUNCIONA EL PROGRAMA
A. El programa inicia con un menú de bienvenida, y brinda tres opciones:
1. Iniciar un nuevo juego preconfigurado (este será con 6 palabras y una matriz de 10x10 letras).
2. Configurar su propio juego, esto permite:
    - Escoger entre tres posibles tamaños de matriz (10x10, 15x15, 20x20).
    - Utilizar las palabras que el usuario desee. Estos los puede agregar dentro del archivo 'palabras.txt'.
3. Cerrar sesión.

B. Una vez que el usuario haya iniciado un nuevo juego, ya sea preconfigurado o configurado por el usuario mismo, el código funciona de la misma manera.

1. Las palabras que están escondidas dentro de la sopa se imprimen encima de la matriz para que el usuario sepa qué buscar.
2. Se imprime la sopa de letras.
2. El jugador va a estar dentro de un bucle con dos opciones que estarán alternando:
    a) "Ingrese palabras encontradas aquí (una a la vez): "
    b) "Desea seguir? (si / no)? "
El jugador podrá escribir las palabras encontradas dentro de la primera opción (a).
   - Si la palabra encontrada es correcta, se imprime un mensaje indicando que encontró una palabra exitosamente, y esta palabra se imprime en MAYÚSCULA.
   - Si la palabra ingresada no existe, se imprime un mensaje en rojo indicando que esa palabra no existe en la sopa de letras.
Cada vez que el jugador ingresa una palabra, el bucle va a saltar a la siguiente opción (b). Le pregunta si desea seguir o no.
   - Si el usuario indica que SÍ desea seguir, el bucle regresa a la opción de insertar una nueva palabra.
   - Si el usuario indica que NO desea seguir, el bucle termina y van a ocurrir una serie de impresiones.

C. Impresiones finales:
   - Si el encontró e ingresó todas las palabras correctas, se van a imprimir todas las palabras que encontró, y luego se imprime un mensaje indicando que ha ganado.
   - Si el usuario terminó la partida sin ingresar todas las palabras escondidas en la sopa, se van a imprimir todas las palabras encontradas, todas las palabras no encontradas, y un mensaje final indicando que intente de nuevo.
