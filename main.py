"""Main file"""
from function import calculate_voltage, calculate_current, calculate_resistance

def main():
    """- Main call all the functions"""
    while True:
        print("This is a simple calculator for Ohm's Law")

        tax = [
            "Press",
            "1. To check for voltage (V)",
            "2. To check for current (I)",
            "3. To check for Resistance (R)\n"
        ]
        for my_tax in tax:
            print(my_tax)

        user_input = input("$ ")

        if user_input == "1":
            print("====================================")
            calculate_voltage()
            print("====================================\n")
        elif user_input == "2":
            print("====================================")
            calculate_current()
            print("====================================\n")
        elif user_input == "3":
            print("====================================")
            calculate_resistance()
            print("====================================\n")
        else:
            print("\nInvalid input.........\n")

if __name__ == "__main__":
    main()
