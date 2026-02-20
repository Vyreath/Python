palabra = input("Escribe una palabra: ")
esisograma = True

for i in range (0,len(palabra)):

    letra = palabra[i].lower()

    for j in range (0,len(palabra)):

        if letra == palabra[j].lower() and i != j :
            esisograma = False
            break
    if esisograma == False:
        break

print(esisograma)
