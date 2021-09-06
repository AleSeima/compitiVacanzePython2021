def main():

    stringa1 = "bottles of beer on the wall, bottles of beer."
    stringa2 = "Take one down and pass it around, 98 bottles of beer on the wall."
    cnt = 99

    for k in range(100):
        if cnt < 1:
            print("No more bottles of beer on the wall, no more bottles of beer.")
        else:
            print(f"{cnt} bottles of beer on the wall, {cnt} bottles of beer.")

        if cnt-1 < 1:
            if cnt-1 < 0:
                print("Go to the store and buy some more, 99 bottles of beer on the wall.")
            else:
                print(f"Take one down and pass it around, no more bottles of beer on the wall.")
        else:
            print(f"Take one down and pass it around, {cnt-1} bottles of beer on the wall.")
        cnt = cnt-1

if __name__ == "__main__":
    main()