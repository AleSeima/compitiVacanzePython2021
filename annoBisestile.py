def main():

    anno = int(input("Inserire l'anno da verificare"))

    if anno % 4 == 0:
        if anno % 100 == 0:
            if anno % 400 == 0:
                print("Anno bisestile")
            else:
                print("Anno NON bisestile")
        else:
            print("Anno NON bisestile")
    else:
        print("Anno NON bisestile")

        
if __name__ == "__main__":
    main()