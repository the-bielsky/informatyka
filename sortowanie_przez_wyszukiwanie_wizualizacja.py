"""Edukacyjna wizualizacja sortowania przez proste wybieranie.

Uruchom ten plik w terminalu. Enter pokazuje kolejny krok.
Algorytm wybiera minimum z nieposortowanej czesci i przenosi je na poczatek.
Czas: O(n^2), dodatkowa pamiec samego algorytmu: O(1).
"""



def pokaz_krok(numbers, opis, posortowane=0, min_idx=None, sprawdzany=None):
    szerokosc = max(2, max((len(str(n)) for n in numbers), default=0))
    krawedz = "+" + "-" * (szerokosc + 2) + "+"
    ramka = " ".join(krawedz for _ in numbers)

    print("\n" + opis)
    if not numbers:
        print("(pusta lista)")
        return

    print(ramka)
    print(" ".join(f"| {n:>{szerokosc}} |" for n in numbers))
    print(ramka)

    oznaczenia = []
    for indeks in range(len(numbers)):
        if indeks < posortowane:
            znak = "OK"
        else:
            znak = "M" if indeks == min_idx else ""
            if indeks == sprawdzany:
                znak += "?"
        oznaczenia.append(f"{znak:^{szerokosc + 4}}")
    print(" ".join(oznaczenia))
    if posortowane < len(numbers):
        input("\nEnter - nastepny krok...")


def sortowanie_przez_wybieranie(numbers):
    """Sortuje liste rosnaco w miejscu, pokazujac porownania i zamiany."""
    print("SORTOWANIE PRZEZ PROSTE WYBIERANIE")
    print("OK - gotowa czesc | M - minimum | ? - sprawdzany element")
    print("M? oznacza, ze sprawdzany element zostal nowym minimum.")
    pokaz_krok(numbers, "Lista poczatkowa:")

    for i in range(len(numbers) - 1):
        min_idx = i
        pokaz_krok(
            numbers,
            f"Przebieg {i + 1}: szukamy minimum od pozycji {i + 1}.",
            i, min_idx,
        )

        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_idx]:
                opis = (
                    f"{numbers[j]} < {numbers[min_idx]}: "
                    f"nowe minimum na pozycji {j + 1}."
                )
                min_idx = j
            else:
                opis = (
                    f"{numbers[j]} >= {numbers[min_idx]}: "
                    "minimum pozostaje bez zmian."
                )
            pokaz_krok(numbers, opis, i, min_idx, j)

        if min_idx != i:
            opis = (
                f"Zamieniamy {numbers[i]} (pozycja {i + 1}) "
                f"z {numbers[min_idx]} (pozycja {min_idx + 1}). "
                f"Pozycja {i + 1} jest gotowa."
            )
            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
        else:
            opis = f"Minimum jest juz na pozycji {i + 1}. Bez zamiany."
        pokaz_krok(numbers, opis, i + 1)

    pokaz_krok(
        numbers,
        "Gotowe! Lista jest posortowana.",
        len(numbers),
    )
    return numbers


if __name__ == "__main__":
    numbers = [5, 2, 9, 1, 5, 6, 3, 8]
    sortowanie_przez_wybieranie(numbers)