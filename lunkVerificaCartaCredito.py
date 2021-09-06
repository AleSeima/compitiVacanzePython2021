def main():
    numero = input("Inserire il numero della carta: ")

    numeroIntero = []   #lista di numeri senza spazi

    for k in numero:    #for per eliminare gli spazi tra i numeri
        if (k != " "):
            numeroIntero.append(k)

    print(f"1: {numeroIntero}")
    k = 15

    while(k > 0):       #while per raddoppiare una cifra ogni due come prevede la formula
        k = k-1
        numeroIntero[k] = int(numeroIntero[k])*2
        if int(numeroIntero[k])>9:
            numeroIntero[k] = int(numeroIntero[k])-9
        
        k = k-1

    print(f"2: {numeroIntero}")

    somma = 0
    k=0

    for k in range(len(numeroIntero)):      #for fatto per sommare i numero
        somma = somma + int(numeroIntero[k])
        k = k + 1

    print(f"La somma dei numeri è: {somma}")
    if(somma % 10 == 0):
        print("Numero di carta valido")
    else:
        print("Numero di carta non valido")

if __name__ == "__main__":
    main()