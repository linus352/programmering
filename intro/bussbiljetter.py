print(" Hur gammal är du")

age = input()
age = int (age)

if age < 7-19:
    print("21 kr")

elif age >= 7 and age <19:
    print("kostar 21 kr")

elif age >= 0 and age <6:
    print("Det kostar 21 kr")

elif age >= 65:
    print("Priset är 21 kr")

elif age >= 19 and age <65:
    print("om man är vuxen kostar det 32 kr")