from ksiazka import Ksiazka

class Biblioteka:
    def __init__(self):
        self.ksiazki = []

    def dodaj_ksiazke(self, tytul, autor, rok_wydania, gatunek):
        ksiazka = Ksiazka(tytul, autor, rok_wydania, gatunek)
        self.ksiazki.append(ksiazka)
        print(f"Dodano książkę: {ksiazka}")

    def edytuj_ksiazke(self, indeks, tytul=None, autor=None, rok_wydania=None, gatunek=None):
        if 0 <= indeks < len(self.ksiazki):
            ksiazka = self.ksiazki[indeks]
            ksiazka.edytuj_ksiazke(tytul, autor, rok_wydania, gatunek)
            print(f"Edytowano książkę: {ksiazka}")
        else:
            print("Nie ma książki o podanym indeksie.")

    def usun_ksiazke(self, indeks):
        if 0 <= indeks < len(self.ksiazki):
            ksiazka = self.ksiazki.pop(indeks)
            print(f"Usunięto książkę: {ksiazka}")
        else:
            print("Nie ma książki o podanym indeksie.")

    def wyswietl_ksiazki(self):
        if self.ksiazki:
            print("\nKsiążki w bibliotece:")
            for indeks, ksiazka in enumerate(self.ksiazki):
                print(f"{indeks}. {ksiazka}")
        else:
            print("Brak książek w bibliotece.")
