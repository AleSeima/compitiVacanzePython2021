def main():

    secondi = int(input("Inserire i secondi: "))

    minuti = secondi/60

    ore = minuti/60

    giorni = ore/24

    anni = giorni/365,25

    print(f"Anni terrestri: {anni}")

if __name__ == "__main__":
    main()