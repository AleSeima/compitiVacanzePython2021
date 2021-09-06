def main():

    numero = input("Inserire il numero di telefono: ")
    numneroFinale = ""

    for cifra in numero:
        if cifra >= "0" and cifra <= "9":
            numneroFinale += cifra

    print(numneroFinale)


if __name__ == "__main__":
    main()