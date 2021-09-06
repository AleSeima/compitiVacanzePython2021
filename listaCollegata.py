def main():

    lista = [] #lista vuota

    for k in range(10):
        lista.append(k)

    print(f"Lista iniziale: {lista}")

    comando = input("Inserire l'operazione della pila: ")

    if comando == "push":

        carattere = input("Inserire l'elemento da inserire nella lista: ")
        lista.append(carattere)
        print("Inserisce l'elemento al fondo della lista")

    if comando == "pop":

        lista.pop()
        print("Rimuove l'elemento al fondo della lista")

    if comando == "shift":

        lista.pop(0)
        print("Rimuove l'elemento all'inizio della lista")

    if comando == "unshift":

        carattere = input("Inserire l'elemento da inserire nella lista: ")
        lista.insert(0, carattere)
        print("Inserisce l'elemento all'inizio della lista")

    print(f"Lista finale: {lista}")
    

if __name__ == "__main__":
    main()