def main():

    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    cifrario = int(input("Inserire il cifrario rotazionale: ROT"))

    frase = input("Inserire la frase: ")

    lettera = 0
    letteraApp = 0
    fraseFinale = ""

    for k in range(len(frase)):
        if frase[k] >= "a" and frase[k] <= "z":
            for j in range(len(alfabeto)):
                if frase[k] == alfabeto[j]:
                    lettera = j

            letteraApp = lettera + cifrario

            if letteraApp > 26:
                letteraApp = cifrario - (len(alfabeto)-lettera)
            
            fraseFinale += alfabeto[letteraApp]
        else:
            fraseFinale += frase[k]

        lettera = 0
        letteraApp = 0

    print(f"La frase finale è: {fraseFinale}")

if __name__ == "__main__":
    main()