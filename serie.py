def main():

    stringa = input("Inserire la stringa di numeri: ")
    n = int(input("Inserire la serie delle cifre: "))
    strAppoggio = ""

    for k in range(len(stringa)):
        if len(stringa) - k >= n:
            for j in range(n):
                strAppoggio += stringa[k+j]

            print(strAppoggio)

            strAppoggio = ""

        
if __name__ == "__main__":
    main()