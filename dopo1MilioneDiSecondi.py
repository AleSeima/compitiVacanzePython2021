def main():

    dataAnno = int(input("Inserire l'anno della data: "))
    dataMese = int(input("Inserire il mese della data: "))
    dataGiorno = int(input("Inserire il giorno della data: "))
    timeOra = int(input("Inserire le ore dell'orario: "))
    timeMinuti = int(input("Inserire i minuti dell'orario: "))
    timeSecondi = int(input("Inserire i secondi dell'orario: "))
    timeMinutiNuovo = 0
    timeOraNuovo = 0
    giorniNuovo = 0
    meseNuovo = 0
    annoNuovo = 0

    minutiRimanenti = 0.77777 / 60
    secondiRimanenti = 0.662/60

    timeMinuti = timeMinuti + (timeOra*60)

    timeSecondi = timeSecondi + (timeMinuti*60)

    timeSecondi = timeSecondi + 1000000

    timeMinutiNuovo = timeMinutiNuovo + (timeSecondi/60)

    timeOraNuovo = timeOraNuovo + (timeMinutiNuovo/60)

    giorniNuovo = dataGiorno + (timeOraNuovo/24)

    if giorniNuovo > 31:
        dataMese = dataMese + 1
        giorniNuovo = giorniNuovo - 31

    timeOra = (timeOra + 7)-277

    if timeOra > 24:
        giorniNuovo = giorniNuovo + 1
        timeOra = timeOra - 24

    if meseNuovo > 12:
        dataMese = dataMese-12
        dataAnno = dataAnno+1

    timeMinutiNuovo = timeMinutiNuovo - 16666

    if timeMinutiNuovo > 60:
        timeOraNuovo = timeOraNuovo + 1
        timeMinutiNuovo = timeMinutiNuovo - 60
    

    print(timeMinutiNuovo)
    print(timeOraNuovo)
    print(giorniNuovo)
    
    print("DATA FINALE: ")
    print(F"{round(giorniNuovo)}/{round(dataMese)}/{round(dataAnno)}")
    print("ORA: ")
    print(f"{round(timeOraNuovo)}:{round(timeMinutiNuovo)}:{round(timeMinutiNuovo)}")


if __name__ == "__main__":
    main()