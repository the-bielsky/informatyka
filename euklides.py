def main():
liczba1 = int(input("Wprowadź pierwszą liczbę: "))
liczba2 = int(input("Wprowadź drugą liczbę: "))
print("NWD dla liczb", liczba1, "i", liczba2, "wynosi:",
NWD_odejmowanie(liczba1,liczba2))
print("NWD dla liczb", liczba1, "i", liczba2, "wynosi:",
NWD_dzielenie(liczba1,liczba2))
def NWD_odejmowanie(a, b):
licznik_petli = 0
while a != b:
if a > b:
a -= b
else:
b -= a
licznik_petli += 1
print("_______________________________________________________")
print("Wersja z odejmowaniem")
print("Ilość wykonanych działań:", licznik_petli)
return a
def NWD_dzielenie(a, b):
... #Uzupełnij kod dla wersji z dzieleniem!!! pamiętaj o
liczeniu wykonań pętli.
print("_______________________________________________________")
print("Wersja z dzieleniem")
print("Ilość wykonanych działań:", licznik_petli)
return a
main()