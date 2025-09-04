print("Det finns glass för 20 kr")
print("varmkorv för 15 kr")
print("läsk för 15 kr")
print("godis för 10 kr")

item = input()

if item == "Glass":
    print(" Hur många glassar vill du ha")
    amount = input()
    amount = int ( amount)
    price = amount * 20
    print("Det blir", price, "kronor")

elif item == "varmkorv":
    print(" Hur många varmkorvar vill du ha")
    amount = input()
    amount = int ( amount)
    price = amount * 15
    print("Det blir", price, "kronor")


elif item == "läsk":
    print(" Hur många läskar vill du ha")
    amount = input()
    amount = int ( amount)
    price = amount * 15
    print("Det blir", price, "kronor")

elif item == "godis":
    print(" Hur mycket godis vill du ha")
    amount = input()
    amount = int ( amount)
    price = amount * 10
    print("Det blir", price, "kronor")
