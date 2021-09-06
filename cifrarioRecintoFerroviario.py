def main():

    stringa = input("Inserire la stringa: ")

    riga1 = []
    riga2 = []
    riga3 = []
    cntRiga3 = 6

    for let in range(len(stringa)):
        if let == 0:
            riga1.append(stringa[let])
        if let % 4 == 0:
            riga1.append(stringa[let])
        if let % 2 != 0:
            riga2.append(stringa[let])
        if let == 2:
            riga3.append(stringa[let])
        if cntRiga3 == let:
            riga3.append(stringa[let])
            cntRiga3 = cntRiga3 + 4

    print(riga1)
    print(riga2)
    print(riga3)


if __name__ == "__main__":
    main()