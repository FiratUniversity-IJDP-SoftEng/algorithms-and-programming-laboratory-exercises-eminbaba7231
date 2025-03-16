# Your Student ID:230543008
# Your Name and Surname:Emin Talha Celik
conversion_type = input("Enter conversion type (C to F or F to C): ").strip().lower()
temperature = float(input("Enter the temperature value: "))
if conversion_type == "c to f":
    result = (temperature * 9/5) + 32
    print(f"{temperature} Celsius is {result} Fahrenheit")
elif conversion_type == "f to c":
    result = (temperature - 32) * 5/9
    print(f"{temperature} Fahrenheit is {result} Celsius")
else:
    print("Invalid conversion type")
