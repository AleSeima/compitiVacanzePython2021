def main():

    lato1 = int(input("Inserire la lunghezza del primo lato: "))
    lato2 = int(input("Inserire la lunghezza del secondo lato: "))
    lato3 = int(input("Inserire la lunghezza del terzo lato: "))

    if lato1 > 0 and lato2 > 0 and lato3 > 0:

        if lato1 + lato2 >= lato3 or lato1 + lato3 >= lato2 or lato3 + lato2 >= lato1:

            if lato1 + lato2 == lato3 or lato1 + lato3 == lato2 or lato3 + lato2 == lato1:
                print("TRIANGOLO DEGENERE")

            if lato1 == lato2 and lato2 == lato3 and lato3 == lato1:
                print("TRIANGOLO EQUILATERO")

            if lato1 == lato2:
                if lato2 != lato3 or lato1 != lato3:
                    print("TRIANGOLO ISOSCELE")

            if lato2 == lato3:
                if lato1 != lato3 or lato1 != lato2:
                    print("TRIANGOLO ISOSCELE")

            if lato1 == lato3:
                if lato1 != lato2 or lato3 != lato2:
                    print("TRIANGOLO ISOSCELE")

            if lato1 != lato2 and lato2 != lato3 and lato3 != lato1:
                print("TRIANGOLO SCALENO")

if __name__ == "__main__":
    main()