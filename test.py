def ohms_law_calculator():
    """Calculates voltage, current, or resistance using Ohm's Law."""

    while True:
        print("\nOhm's Law Calculator")
        print("1. Calculate Voltage")
        print("2. Calculate Current")
        print("3. Calculate Resistance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "4":
            break

        try:
            if choice == "1":
                current = float(input("Enter current (in Amperes): "))
                resistance = float(input("Enter resistance (in Ohms): "))
                voltage = current * resistance
                print("Voltage = ", voltage, "Volts")
            elif choice == "2":
                voltage = float(input("Enter voltage (in Volts): "))
                resistance = float(input("Enter resistance (in Ohms): "))
                current = voltage / resistance
                print("Current = ", current, "Amperes")
            elif choice == "3":
                voltage = float(input("Enter voltage (in Volts): "))
                current = float(input("Enter current (in Amperes): "))
                resistance = voltage / current
                print("Resistance = ", resistance, "Ohms")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numerical values only.")

if __name__ == "__main__":
    ohms_law_calculator()
