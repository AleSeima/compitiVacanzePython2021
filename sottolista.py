def main():

    elementiLista1 = input("Inserire gli elementi della prima lista: ")
    elementiLista2 = input("Inserire gli elementi della seconda lista: ")

    listaA = []
    listaB = []

    ugualeA = True
    ugualeB = True
    presente = True

    cnt1 = 0
    cnt2 = 0

    for k1 in elementiLista1:
        listaA.append(k1)

    for k2 in elementiLista2:
        listaB.append(k2)

    for el1 in listaA:
        for el2 in listaB:
            if el1 == el2:
                print("CIAO1")
                presente = True
                cnt1 = cnt1 + 1
                break
        if presente == True:
            print("CIAO2")
            ugualeA = True
        else:
            ugualeA = False
            print("CIAONO")
    
    for el2 in listaA:
        for el1 in listaB:
            if el2 == el1:
                print("CIAO3")
                presente = True
                cnt2 = cnt2 + 1
                break
        if presente == True:
            print("CIAO4")
            ugualeB = True
        else:
            ugualeB = False
            print("CIAONO")

    print(ugualeA)
    print(ugualeB)
    if len(elementiLista1) == len(elementiLista2):
        if ugualeA == True and ugualeB == True:
            print("Le liste sono uguali")

    if len(elementiLista1) > len(elementiLista2):
        if ugualeA == True and ugualeB == True:
            print("La lista B è una sottolista della lista A")

    if len(elementiLista1) < len(elementiLista2):
        if ugualeA == True and ugualeB == True:
            print("La lista A è una sottolista della lista B")

    

if __name__ == "__main__":
    main()