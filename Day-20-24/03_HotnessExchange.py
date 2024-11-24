# C = (F- 32 ) * 5 / 9
# F = C * 9/5 + 32


def CelsiusToFahrenheit(C):
    F = (C * 9 / 5) + 32
    print(f"Temperature is: {F}°F")


def FahrenheitToCelsius(F):
    C = (F - 32) * 5 / 9
    print(f"Temperature is: {C}°C")


def KelvinToCelsius(K):
    C = K - 273.15
    print(f"Temperature is: {C}°C")


def CelsiusToKelvin(C):
    K = C + 273.15
    print(f"Temperature is: {K} K")


def main():
    print("Aapka Swagat Hai Hotness Exchange Mein!")
    print("Aaj aap kaunsa trade karna chahenge?")
    options = """ 
    ---- Yeh Hai Aapke Options ----
        1. Kelvin to Celsius
        2. Celsius to Kelvin
        3. Celsius to Fahrenheit
        4. Fahrenheit to Celsius"""
    print(options)

    try:
        operationtype = int(input("Punch Your Trade (1-4): "))
        if operationtype in [1, 2, 3, 4]:
            temperature = float(input("Enter the temperature value: "))
            match operationtype:
                case 1:
                    KelvinToCelsius(temperature)
                case 2:
                    CelsiusToKelvin(temperature)
                case 3:
                    CelsiusToFahrenheit(temperature)
                case 4:
                    FahrenheitToCelsius(temperature)
        else:
            print("Invalid option! Please select a number between 1 and 4.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")


if __name__ == "__main__":
    main()
