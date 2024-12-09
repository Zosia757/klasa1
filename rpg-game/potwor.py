from random import randint

#zombiak
def wygeneruj_potwora() -> list:
    sila = randint(30, 50)
    logiczne_myslenie = 10
    szybkosc = randint(30, 50)
    return [sila, logiczne_myslenie, szybkosc]

#wampir
def wygeneruj_super_potwora() -> list:
    sila = randint(50, 90)
    logiczne_myslenie = 40
    szybkosc = randint(50, 80)
    return [sila, logiczne_myslenie, szybkosc]