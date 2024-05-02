class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_spaces = capacity

    def park_car(self):
        if self.available_spaces > 0:
            self.available_spaces -= 1
            print("Car parked successfully.")
        else:
            print("Sorry, parking lot is full.")

    def vacate_space(self):
        if self.available_spaces < self.capacity:
            self.available_spaces += 1
            print("Parking space vacated successfully.")
        else:
            print("Parking lot is already empty.")

    def display_availability(self):
        print(f"Available parking spaces: {self.available_spaces}/{self.capacity}")


def main():
    capacity = int(input("Enter the capacity of the parking lot: "))
    parking_lot = ParkingLot(capacity)

    while True:
        print("\nMenu:")
        print("1. Park a car")
        print("2. Vacate a parking space")
        print("3. Display availability")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            parking_lot.park_car()
        elif choice == '2':
            parking_lot.vacate_space()
        elif choice == '3':
            parking_lot.display_availability()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
