def main():
    dna = input("Inserire il frammento di DNA: ")

    pilaRna = []
    combRna = ("GCAU")
    cnt = 0

    for k in dna:
        if k == "C":
            cnt = 0
            pilaRna.append(combRna[cnt])

        if k == "G":
            cnt = 1
            pilaRna.append(combRna[cnt])

        if k == "T":
            cnt = 2
            pilaRna.append(combRna[cnt])

        if k == "A":
            cnt = 3
            pilaRna.append(combRna[cnt])

    print(f"RNA: {pilaRna}")

if __name__ == "__main__":
    main()