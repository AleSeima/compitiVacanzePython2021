def main():

    dizPunteggi = {"1" : "A,E,I,O,U,L,N,R,S,T", "2":"D,G", "3":"B, C, M, P", "4":"F, H, V, W, Y", "5":"k", "8":"J,X", "10":"Q,Z"}
    nPunti = 7
    sommaPunti = 0

    parola = input("Inserisci la parola: ")

    for h in parola:
        k=0
        for k in range(nPunti):
            j=0
            for j in range(len(dizPunteggi[k])):
                if dizPunteggi[k][j] == h:
                    sommaPunti = sommaPunti + k   


    print(f"La somma è: {sommaPunti}")             

if __name__ == "__main__":
    main()