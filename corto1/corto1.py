# Corto 1 - Proyectos de progra AIE
# Secuencia de Collatz
# Numero de carne: 201504052
# Numero N maximo 052

max = 52                              # Numero maximo a calcular la secuencia
secuencia = []                        # Almacenamiento de secuencia individual
totalSecuencias = []                  # Almacenamiento de secuencias totales
def detPar(numero):                   # Determinar la paridad por medio de la operacion modulo
    paridad = numero % 2             
    return paridad

for i in range(2, max + 1):           # Ciclo desde 2 hasta maximo
    k = i
    secuencia.append(int(k))          # Agregar numero inicial a la secuencia
    while k > 1:
        par = detPar(k)
        if par == 0:                  # Si el numero es par
            k = k / 2                 # El siguiente toma este valor
            secuencia.append(int(k))  # Se anade el numero a la secuencia
        else:                         # Si no es par
            k = (3 * k) + 1           # El siguiente toma este valor
            secuencia.append(int(k))  # SE anade el numero a la secuencia

    totalSecuencias.append(secuencia) # Se guardan todas las secuencias
    secuencia = []                    # Se limpia el vector para reutilizarlo

collatz = open('collatz.txt', 'w')    # Creacion de archivo
for lista in totalSecuencias:         # Recorre cada lista dentro de todas las listas
    collatz.write(str(lista) + '\n')  # Escribe cada lista y un salto de linea

collatz.close()                       # CIerra el archivo
print(totalSecuencias)