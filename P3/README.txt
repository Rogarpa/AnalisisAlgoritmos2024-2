El programa está implementado en el lenguaje python (3)
Para correr el programa con las variables default:
$python3 main.py
Para correr el programa con el archivo input.txt (incluido) como entrada:
$python3 main.py -f input.txt
    Nota: El formato debe ser:
    Primera linea numeros separados por una coma
    Segunda linea elementos (palabras) separados con una coma (para RadixLSD)
    Tercera linea longitud de los elementos para RadixLSD

Para correr el programa introduciendo las secuencias a ordernar correr:
$python3 main.py -a [1,2,3] ["011","101","093","004","z31","z22","z13"] 2
    Nota: El primer arreglo es el arreglo que ordenara LocalInsertionSort y TreeSort
    El segundo arreglo es el arreglo que ordenara RadixLSD
    El tercer argumento es la longitud de los elementos para RadixLSD

