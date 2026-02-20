palabra = input("Escribe una palabra: ")
esisograma = True

for i in range (0,len(palabra)):

    letra = palabra[i]

    for j in range (0,len(palabra)):

        if (letra == palabra[j]) and i != j :
            esisograma = False
            break

print(esisograma)
