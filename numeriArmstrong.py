def main():

    numero = input("Inserire un numero: ")

    esponente = len(numero)
    ris = 0

    for k in numero:
        ris = ris + pow(int(k),esponente)

    if ris == int(numero):
        print("E' un numero di Armstrong")
    else:
        print("NON è un numero di Armstrong")


if __name__ == "__main__":
    main()