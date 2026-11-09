def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


temperature = 25

result = celsius_to_fahrenheit(temperature)

print("Temperature Converter")
print(f"{temperature}°C = {result}°F")