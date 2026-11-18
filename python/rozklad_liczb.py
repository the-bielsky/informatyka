def main():
    rozkladana_liczba = int(input("Wprowadź liczbę, którą chcesz "
                                   "rozłożyć na cyfry: "))
    print("Liczba", rozkladana_liczba, "składa się z następujących "
          "cyfr wypisanych od najmniej znaczącej: ", rozklad_na_cyfry(rozkladana_liczba))  # Uzupełnij brakujący kod


def rozklad_na_cyfry(liczba):
    if liczba == 0:
        #...:  # Uzupełnij brakujący kod
        return [ 0 ]
    else:
        cyfry_liczby = []  # Utworzenie listy do przechowywania cyfr
        while liczba > 0:
            #...:  # Uzupełnij brakujący kod
            cyfry_liczby.append(liczba % 10)  # Uzupełnij brakujący kod,
            # .append odpowiada za dodanie pozycji do listy
            liczba //= 10  # Uzupełnij brakujący kod
            # liczba = liczba // 10
        return cyfry_liczby  # Uzupełnij brakujący kod

main()