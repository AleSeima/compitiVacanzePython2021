def main():

    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabetoInv = "zyxwvutsrqponmlkjihgfedcba"

    stringa = input("Inserire la frase")
    stringaDecodificata = ""

    for let in stringa:
        if let >= "a" and let <= "z":
            for j in range(len(alfabeto)):
                if let == alfabeto[j]:
                    stringaDecodificata += alfabetoInv[j]

        else:
            stringaDecodificata += let

    print(f"La stringa decodi: {stringaDecodificata}")

if __name__ == "__main__":
    main()