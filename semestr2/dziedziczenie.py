class Pojazd:
    def __init__(self, marka, model, rok_produkcji, kolor):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.kolor = kolor

    def przedstaw_sie(self):
        print(f"To jest {self.marka} {self.model}, {self.rok_produkcji} r., kolor: {self.kolor}.")

    def uruchom_silnik(self):
        print(f"Silnik {self.marka} {self.model} uruchomiony!")


class SamochodOsobowy(Pojazd):
    def __init__(self, marka, model, rok_produkcji, kolor, liczba_drzwi, typ_napędu):
        super().__init__(marka, model, rok_produkcji, kolor)
        self.liczba_drzwi = liczba_drzwi
        self.typ_napędu = typ_napędu

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Jest to samochód osobowy z {self.liczba_drzwi} drzwiami, napęd: {self.typ_napędu}.")

    def uruchom_silnik(self):
        super().uruchom_silnik()
        print("Pojazd jest gotowy do jazdy!")


class Motocykl(Pojazd):
    def __init__(self, marka, model, rok_produkcji, kolor, typ):
        super().__init__(marka, model, rok_produkcji, kolor)
        self.typ = typ

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"To motocykl typu {self.typ}.")

    def uruchom_silnik(self):
        super().uruchom_silnik()
        print("Motocykl jest gotowy do jazdy!")


class PojazdElektryczny(Pojazd):
    def __init__(self, marka, model, rok_produkcji, kolor, zasięg_na_baterii):
        super().__init__(marka, model, rok_produkcji, kolor)
        self.zasięg_na_baterii = zasięg_na_baterii

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Jest to pojazd elektryczny z zasięgiem na baterii: {self.zasięg_na_baterii} km.")

    def uruchom_silnik(self):
        super().uruchom_silnik()
        print("Pojazd elektryczny jest gotowy do jazdy!")


class PojazdHybrydowy(PojazdElektryczny):
    def __init__(self, marka, model, rok_produkcji, kolor, zasięg_na_baterii, typ_napędu):
        super().__init__(marka, model, rok_produkcji, kolor, zasięg_na_baterii)
        self.typ_napędu = typ_napędu

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"To pojazd hybrydowy z napędem {self.typ_napędu}.")

    def uruchom_silnik(self):
        super().uruchom_silnik()
        print("Pojazd hybrydowy jest gotowy do jazdy!")


class TestPojazdów:
    def __init__(self):
        self.pojazdy = []

    def dodaj_pojazd(self, pojazd):
        self.pojazdy.append(pojazd)

    def uruchom_wszystkie_silniki(self):
        for pojazd in self.pojazdy:
            pojazd.uruchom_silnik()

    def przedstaw_wszystkie_pojazdy(self):
        for pojazd in self.pojazdy:
            pojazd.przedstaw_sie()


def main():

    samochod = SamochodOsobowy("Toyota", "Corolla", 2020, "czerwony", 4, "spalinowy")
    motocykl = Motocykl("Harley-Davidson", "Sportster", 2019, "czarny", "cruiser")
    elektryk = PojazdElektryczny("Tesla", "Model 3", 2023, "biały", 500)
    hybryda = PojazdHybrydowy("Toyota", "Prius", 2022, "zielony", 400, "hybrydowy")

    tester = TestPojazdów()

    tester.dodaj_pojazd(samochod)
    tester.dodaj_pojazd(motocykl)
    tester.dodaj_pojazd(elektryk)
    tester.dodaj_pojazd(hybryda)

    tester.przedstaw_wszystkie_pojazdy()

    tester.uruchom_wszystkie_silniki()

if __name__ == "__main__":
    main()
