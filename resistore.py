def main():
    colore1 = input("Inserire il primo colore: ")
    colore2 = input("Inserire il secondo colore: ")

    pilaRisultato = []
    listaColori = ["nero", "marrone", "rosso", "arancione", "giallo", "verde", "blu", "viola", "grigio", "bianco"]
    cnt = 0
    k=0

    for k in listaColori:
        if (k == colore1):
            pilaRisultato.append(cnt)

        cnt = cnt + 1
    
    cnt=0

    for k in listaColori:
        if (k == colore2):
            pilaRisultato.append(cnt)

        cnt = cnt + 1
    
    print(f"VALORE RESISTENZA: {pilaRisultato[0]}{pilaRisultato[1]}")

if __name__ == "__main__":
    main()