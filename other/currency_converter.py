pesos = input("Insert pesos: ")
pesos = float(pesos)

print(f"\ndebug: pesos to float {pesos}")

a_dolar_value_from_peso = 123

dolars = pesos / a_dolar_value_from_peso
# print(f"debug: dolars from pesos {dolars}")
dolars = round(dolars,2)
# print(f"debug: dolars rounded {dolars}")
dolares = str(dolars)
# print(f"debug: dolars to string {dolars}")

print(f"\nFriend actually you have {dolars} dolars")