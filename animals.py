def main():
    while True:
        ## Skriv ut menyvalen
        print("1. Cat")
        print("2. Cow")
        print("Enter x to exit")

        choice = input("Enter your selection")
        match choice.lower():
            case '1': #Cat-sound
                print("Mjau, mjau")
            case '2': #Cow-sound
                print("Muu, muu")
            case 'x': #Exit
                break
            case _:
                print(f"Unrecognized input {choice}")

if __name__ == '__main__':
    main()
