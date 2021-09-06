def main():

    quadrato = int(input("Inserire il numero del quadrato: "))

    nQuadrati = 64
    sommaCicchiTot = 0
    nChicchiQuadrato = 0

    for k in range(nQuadrati):
        sommaCicchiTot = sommaCicchiTot + pow(2,k)

        if k == quadrato:
            nChicchiQuadrato = pow(2,k)

    print(f"In totale su tutta la scacchiera ci sono: {sommaCicchiTot} chicchi.\nSul quadrato n {quadrato} ci sono {nChicchiQuadrato} chicchi.")

if __name__ == "__main__":
    main()