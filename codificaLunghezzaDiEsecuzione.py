def main():

    stringa = input("Inserire la stringa estesa: ")
    pilaStringaFinale = []
    pilaStringaFinale2 = []
    cnt = 1
    k=0
    primoGiro = False
    lettera = 1

    for lettera in range(len(stringa)):

        if stringa[lettera] == stringa[lettera-1]:
            cnt = cnt + 1

        else:
            if primoGiro == False:
                if cnt > 1:
                    pilaStringaFinale.append(cnt)
                    pilaStringaFinale.append(stringa[lettera-1])
                else:
                    pilaStringaFinale.append(stringa[lettera])
                primoGiro = True
                pilaStringaFinale.pop()

            else:
                if cnt > 1:
                    pilaStringaFinale.append(cnt)
                    pilaStringaFinale.append(stringa[lettera-1])
                else:
                    pilaStringaFinale.append(stringa[lettera-1])

            cnt = 1
        k = k+1         

        if k == len(stringa):
            print("CIAO")
            if cnt > 1:
                pilaStringaFinale.append(cnt)
                pilaStringaFinale.append(stringa[lettera])
            else:
                pilaStringaFinale.append(stringa[lettera])   
        
    '''
    primaLettera = pilaStringaFinale.pop()
    if primaLettera >= "a" and primaLettera <= "z":
        pilaStringaFinale.append(primaLettera)
    else:
        pilaStringaFinale.append(primaLettera)
        primaLettera = pilaStringaFinale.pop()
        pilaStringaFinale.append(primaLettera)
    '''

    stringa2 = input("Inserire la stringa compattata: ")

    for lettera in range(len(stringa2)):
        if (stringa2[lettera] >= "a" and stringa2[lettera] <= "z"):
            pilaStringaFinale2.append(stringa2[lettera])
        else:
            for k in range(int(stringa2[lettera])-1):
                pilaStringaFinale2.append(stringa2[lettera+1])


    print(pilaStringaFinale)    
    print(pilaStringaFinale2)    

if __name__ == "__main__":
    main()