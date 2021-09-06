def main():
    stringa = input("Inserire la stringa: ")

    stringaAppoggio = ""
    k = len(stringa)
    j = 0

    while k>0:
        stringaAppoggio += stringa[k-1]
        k = k-1
        j = j+1

    print(f"La stringa al contrario è: {stringaAppoggio}")

if __name__ == "__main__":
    main()