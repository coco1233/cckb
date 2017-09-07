input =raw_input(" Enter Celsius or Fahrenheit?(C/F):")

enter = float(raw_input("Enter temperature:"))
if input == 'C':
    Fahrenheit = enter * 9.0 / 5 + 32
    print enter , "celsius is converted to fahrenheit:" , Fahrenheit
else:
    Celsius = enter - 32 * 5 / 9
    print enter , "fahrenheit is converted to celsius:" , Celsius
if input not in ('C','F'):
    exit()
