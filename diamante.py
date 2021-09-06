def main():

    letteraFinale = input("Inserire la lettera: ")
    alfabeto = " abcdefghilmnopqrstuvz"

    k = 1

    for k in range(len(alfabeto)):
        if letteraFinale == alfabeto[k]:
            numeroLetteraFinale = k

    k = 1

    cnt = 1

    for cnt in range(numeroLetteraFinale*4):
        if cnt == 1:
            k = 1
            for k in range((numeroLetteraFinale*2)):
                if k == numeroLetteraFinale:
                    print(alfabeto[1], end='')
                else:
                    print(" ", end='')

        if cnt <= numeroLetteraFinale:

            k = 1

            for k in range((numeroLetteraFinale*2)+1):
                if k <= numeroLetteraFinale/2:
                    if k == numeroLetteraFinale - cnt:
                        print(alfabeto[cnt], end='')
                    else:
                        print(" ", end='')
                else:
                    if k - cnt == 4:
                        print(alfabeto[cnt], end='')
                    else:
                        print(" ", end='')

        else:

            k = 1
            cont = 0
            let = 0
            for k in range((numeroLetteraFinale)):
                cont = cont+1
                if k <= numeroLetteraFinale:
                    if cnt - k == 4:
                        let = let + 1
                        print(alfabeto[numeroLetteraFinale-(cnt-numeroLetteraFinale)], end='')
                    else:
                        print(" ", end='')
                else:
                    print(" ", end='')

        
        print("\n")
        

    print(cont)
    print(let)

if __name__ == "__main__":
    main()