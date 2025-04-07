class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania, gatunek):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek

    def __str__(self):
        return f"{self.tytul} ({self.rok_wydania}) - {self.autor} ({self.gatunek})"

    def edytuj_ksiazke(self, tytul=None, autor=None, rok_wydania=None, gatunek=None):
        if tytul:
            self.tytul = tytul
        if autor:
            self.autor = autor
        if rok_wydania:
            self.rok_wydania = rok_wydania
        if gatunek:
            self.gatunek = gatunek
