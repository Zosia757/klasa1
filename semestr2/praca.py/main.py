from biblioteka import Biblioteka

def menu():
    print("\nWybierz opcję:")
    print("1. Dodaj książkę")
    print("2. Edytuj książkę")
    print("3. Usuń książkę")
    print("4. Wyświetl książki")
    print("5. Zakończ")

def dodaj_ksiazke(biblioteka):
    tytul = input("Tytuł książki: ")
    autor = input("Autor książki: ")
    rok_wydania = input("Rok wydania: ")
    gatunek = input("Gatunek książki: ")
    biblioteka.dodaj_ksiazke(tytul, autor, rok_wydania, gatunek)

def edytuj_ksiazke(biblioteka):
    biblioteka.wyswietl_ksiazki()
    try:
        indeks = int(input("Wybierz numer książki do edytowania: "))
        tytul = input("Nowy tytuł (lub wciśnij Enter, aby nie zmieniać): ")
        autor = input("Nowy autor (lub wciśnij Enter, aby nie zmieniać): ")
        rok_wydania = input("Nowy rok wydania (lub wciśnij Enter, aby nie zmieniać): ")
        gatunek = input("Nowy gatunek (lub wciśnij Enter, aby nie zmieniać): ")
        biblioteka.edytuj_ksiazke(indeks, tytul if tytul else None, autor if autor else None,
                                  rok_wydania if rok_wydania else None, gatunek if gatunek else None)
    except ValueError:
        print("Nieprawidłowy numer książki.")

def usun_ksiazke(biblioteka):
    biblioteka.wyswietl_ksiazki()
    try:
        indeks = int(input("Wybierz numer książki do usunięcia: "))
        biblioteka.usun_ksiazke(indeks)
    except ValueError:
        print("Nieprawidłowy numer książki.")

def main():
    biblioteka = Biblioteka()

    while True:
        menu()
        wybor = input("Wybór: ")

        if wybor == "1":
            dodaj_ksiazke(biblioteka)
        elif wybor == "2":
            edytuj_ksiazke(biblioteka)
        elif wybor == "3":
            usun_ksiazke(biblioteka)
        elif wybor == "4":
            biblioteka.wyswietl_ksiazki()
        elif wybor == "5":
            print("Zakończenie programu.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()





# Wyjaśnienie:

# Ksiazka (klasa):
# Przechowuje informacje o książce: tytuł, autor, rok wydania, gatunek.
# Metoda edytuj_ksiazke() pozwala na edytowanie danych książki.

# Biblioteka (klasa):
# Zawiera listę książek.
# Metody: dodaj_ksiazke(), edytuj_ksiazke(), usun_ksiazke(), wyswietl_ksiazki() umożliwiają zarządzanie książkami w bibliotece.

# main.py:
# Zapewnia interfejs tekstowy dla użytkownika do dodawania, edytowania, usuwania książek oraz wyświetlania zawartości biblioteki.