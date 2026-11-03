cars = {"Toyota": 50, "Honda": 45, "BMW": 80, "Ford": 40, "Audi": 90}

rented = []


def view_available_cars():
    for car in cars:
        if car not in rented:
            print(f"{car} - ${cars[car]} per day")


def rent_car():
    car = input("Enter car name: ")
    if car in cars:
        if car not in rented:
            days = int(input("Enter number of days: "))
            rented.append(car)
            total = cars[car] * days
            print(f"{car} rented for {days} days. Total: ${total}")
        else:
            print(f"{car} is already rented")
    else:
        print(f"{car} does not exist")


def return_car():
    car = input("Enter car name: ")
    if car in rented:
        rented.remove(car)
        print(f"{car} has been returned")
    else:
        print(f"{car} is not rented")


def view_rented_cars():
    for car in rented:
        print(f"{car} is currently rented")


choice = 0
while choice != 5:
    print("1. View available cars")
    print("2. Rent a car")
    print("3. Return a car")
    print("4. View rented cars")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        view_available_cars()
    elif choice == 2:
        rent_car()
    elif choice == 3:
        return_car()
    elif choice == 4:
        view_rented_cars()
    elif choice == 5:
        print("Goodbye")