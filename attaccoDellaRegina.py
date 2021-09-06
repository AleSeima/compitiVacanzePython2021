def main():

    xRegina1 = int(input("Inserire la coordinata x della regina bianca; "))
    yRegina1 = int(input("Inserire la coordinata y della regina bianca; "))
    xRegina2 = int(input("Inserire la coordinata x della regina nera; "))
    yRegina2 = int(input("Inserire la coordinata x della regina nera; "))

    attacco = False

    if xRegina1 == xRegina2:
        attacco = True

    if yRegina1 == yRegina2:
        attacco = True

    if (xRegina1-xRegina2 == yRegina1-yRegina2) or (xRegina2-xRegina1 == yRegina2-yRegina1):
        attacco = True

    if attacco == True:
        print("Le due regine si possono attaccare.")
    else:
        print("Le due regine NON si possono attaccare.")


if __name__ == "__main__":
    main()