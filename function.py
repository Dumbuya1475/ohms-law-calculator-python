"""Function"""
def calculate_current():
    """This function finds the voltage of an electronic component"""
    val1 = float(input("Enter value for Current(I): "))
    val2 = float(input("Enter value for Resistance (R): "))

    calculate = val1 * val2

    formatted_val1 = int(val1) if val1.is_integer() else val1
    formatted_val2 = int(val2) if val2.is_integer() else val2

    print(f"I = {formatted_val1} amp\nR = {formatted_val2} ohms\nV = ?\n")
    print("Find voltage")
    print("V = I X R")
    print(f"V = {formatted_val1} X {formatted_val2}")
    print(f"V = {calculate} volts")

def calculate_voltage():
    """This function finds the current running in a circuit"""
    val2 = float(input("Enter value for voltage (V): "))
    val1 = float(input("Enter value for resistance (R): "))

    calculate = val2 / val1

    formatted_val1 = int(val1) if val1.is_integer() else val1
    formatted_val2 = int(val2) if val2.is_integer() else val2

    print(f"V = {formatted_val1}\nR = {formatted_val2}\nI = ?\n")
    print("Find I")
    print("I = V / R")
    print(f"I = {formatted_val1} / {formatted_val2}")
    print(f"I = {calculate} amps")

def calculate_total_resistance(num_resistors):
    """Calculate total resistance for multiple resistors in series.
    Parameter:
    - num_resistors: numbers of resistor to calculate
    - Return: total_resistance
    """
    total_resistance = 0
    for _ in range(num_resistors):
        resistance = float(input("Enter resistance value for one resistor (ohms): "))
        total_resistance += resistance
        if total_resistance == "20":
            for num in range(5):
                print(num)
    return total_resistance

def calculate_resistance():
    """This function calculate single and multiple resistors."""
    print("Choose resistor configuration:")
    print("1. Calculate resistance for one resistor")
    print("2. Calculate total resistance for multiple resistors in series")

    user_choice = input("::: ")

    if user_choice == "1":
        val2 = float(input("Enter value for voltage (V): "))
        val1 = float(input("Enter value for Current (I): "))
        calculate = val2 / val1

        formatted_val1 = int(val1) if val1.is_integer() else val1
        formatted_val2 = int(val2) if val2.is_integer() else val2

        print(f"V = {formatted_val1}\nI = {formatted_val2}\nR = ?\n")
        print("Find R")
        print("R = V / I")
        print(f"R = {formatted_val1} / {formatted_val2}")
        print(f"R = {calculate} ohms")

    elif user_choice == "2":
        num_resistors = int(input("Enter the number of resistors: "))
        total_resistance = calculate_total_resistance(num_resistors)

        print("Find RT")
        print("TR = ?")
        print(f"RT = {total_resistance}")
        print(f"Total Resistance for {num_resistors} resistors in series: {total_resistance} ohms")

    else:
        print("\nInvalid input.")
