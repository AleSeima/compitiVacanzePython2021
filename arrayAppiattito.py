def main():

    elenco = input("Inserire l'elenco: ")
    elencoAppiattito = ""
    elencoAppiattito += "["

    lungh = 0

    for k in range(len(elenco)):
        if elenco[k] >= "0" and elenco[k] <= "9":
            elencoAppiattito += elenco[k]
        
        if  elenco[k] == ",":
            if elencoAppiattito[lungh-1] != ",":
                elencoAppiattito += elenco[k]

        lungh = len(elencoAppiattito)

    elencoAppiattito += "]"

    print(f"Elenco appiattito: {elencoAppiattito}")

if __name__ == "__main__":
    main()