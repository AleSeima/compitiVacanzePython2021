def main():

    num = int(input("Inserire il numero: "))
    cnt = 0

    while num != 1:
        if num % 2 == 0:
            num = num/2
        else:
            num = (num*3)+ 1
        
        cnt = cnt+1
        
        print(f"{cnt}. {round(num)}")


if __name__ == "__main__":
    main()