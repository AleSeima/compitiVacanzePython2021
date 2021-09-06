def main():

    stringaAzioni = input("Inserire la stringa di azioni del robot: ")

    x = int(input("inserire la coordinata x iniziale: "))

    y = int(input("inserire la coordinata y iniziale: "))

    direzione = input("inserire la direzione iniziale (nord, est, sud, ovest): ")

    for azione in stringaAzioni:

        if direzione == "nord":

            if azione == "a":
                print("AVANTI")
                y = y + 1
            elif azione == "r":
                print("DESTRA")
                direzione = "est"
            elif azione == "l":
                print("SINISTRA")
                direzione = "ovest"
        
        elif direzione == "est":

            if azione == "a":
                print("AVANTI")
                x = x + 1
            elif azione == "r":
                print("DESTRA")
                direzione = "sud"
            elif azione == "l":
                print("SINISTRA")
                direzione = "nord"

        elif direzione == "sud":

            if azione == "a":
                print("AVANTI")
                y = y - 1
            elif azione == "r":
                direzione = "ovest"
                x = x - 1
            elif azione == "l":
                direzione = "est"
                x = x + 1

        elif direzione == "ovest":

            if azione == "a":
                print("AVANTI")
                x = x - 1
            elif azione == "r":
                print("DESTRA")
                direzione = "nord"
            elif azione == "l":
                print("SINISTRA")
                direzione = "sud"

    print(f"Coordinate finali: x: {x},y: {y}.  Direzione finale: {direzione}")

if __name__ == "__main__":
    main()