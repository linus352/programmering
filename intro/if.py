print(" Hur gammal är du ?")

age = input()
age = int(age)

if age < 18:
    print(" Du är ett barn")

elif age == 18:
    print(" Du är 18")

elif age >= 18 and age < 50:
    print(" Du är vuxen")

elif age >= 50:
    print(" Du är gammal")


else:
    print(" Jag vet inte")