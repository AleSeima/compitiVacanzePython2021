def main():

    lista = []
    listaInv = []

    for k in range(11):
        lista.append(k)

    cnt = 10

    for k in lista:
        listaInv.append(lista[cnt])
        cnt = cnt-1

    print(f"Lista iniziale: {lista}")
    print(f"Lista finale: {listaInv}")

if __name__ == "__main__":
    main()