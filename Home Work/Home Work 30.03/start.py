from Lib.db import add_capital, del_capital, show_all_country, edit_capital, edit_population, edit_mayor


def menu():
    while True:
        choice = int(input(
            "1. Add country \n2. Delete country \n3. Show country \n4. Edit capital \n5. Edit population\n6. Edit Mayor\n7. EXIT\n"))
        if choice == 1:
            country = input("Country: ")
            capital = input("Capital: ")
            population = int(input("Population: "))
            Mayor = input("Mayor: ")
            add_capital(country, capital, population, Mayor)
        elif choice == 2:
            country = input("Country: ")
            del_capital(country)
        elif choice == 3:
            show_all_country()
        elif choice == 4:
            country = input("Введіть назву країни ==> ")
            capital = input("Введіть нову столицю == >")
            edit_capital(country, capital)
        elif choice == 5:
            country = input("Введіть назву країни ==> ")
            population = input("Введіть нову кількість населення ==> ")
            edit_population(country, population)
        elif choice == 6:
            country = input("Введіть назву країни ==> ")
            Mayor = input("Введіть ім'я нового мера ==> ")
        elif choice == 7:
            break


menu()
