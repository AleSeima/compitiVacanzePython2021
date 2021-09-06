def main():

    elenco = ["a","b","c","d","e","f","g","h","i","l","m","n","o","p","q","r","s","t","u","v","z"]
    pila = [] #lista vuota per inserire le lettere presenti nella stringa in input

    frase = input("Inserire la frase: ")

    cnt = 0
    presente = False

    for k in frase:
        print(k)
        for j in elenco:
            if k == j:
                for let in pila:
                    if let == k:
                        presente = True

        if presente == False:
            pila.append(k)
            cnt = cnt + 1
            
        presente = False

    if cnt > 20 and cnt < 22:
        print("La frase è un panagramma")
    else:
        print("La frase NON è un panagramma")
        print(f"Numero lettere: {cnt}")

if __name__ == "__main__":
    main()