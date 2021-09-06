def main():
    isbn = input("Inserire l'ISBN: ")

    cnt = 10
    ris = 0

    for k in isbn:
        if k != "-":
            if k == "x" or k == "X":
                k = 10
            ris = ris + int(k)*cnt
            cnt = cnt - 1

    if ris % 11 == 0:
        print("E' un codice ISBN-10")
    else:
        print("Non è un codice ISBN-10")

if __name__ == "__main__":
    main()