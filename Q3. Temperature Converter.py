#Q3.Temperature Converter

#take input in celsius
cel = input("Input temperature in Celsious: ")
print(type(cel))

#celsius convert to float
b = float(cel)      
print(b)
print(type(b))

#Apply formula and calculation(celcius convert to fahrenhight)
f = (b * 9 / 5) + 32
print(f"In Fahrenhite scale: {f}°F")
