#!/usr/bin/env python3
"""
main.py: čtvrtý projekt do kurzu 'Tester s Pythonem'
author: Miroslav Ďuriš
email: miroslav.duris.cze@gmail.com
discord: miroslav_duris

Popis:
Tento skript funguje jako jednoduchý správce úkolů (Task Manager) v příkazové řádce.
Umožňuje uživateli interaktivně spravovat seznam úkolů.

Hlavní funkce aplikace:
1. Přidání nového úkolu (vyžaduje název a popis).
2. Zobrazení všech aktuálních úkolů.
3. Odstranění úkolu podle jeho pořadového čísla.
4. Bezpečné ukončení programu.

Data jsou uchovávána v paměti (list slovníků) po dobu běhu skriptu.
"""

from typing import List, Dict


def zobrazit_nabidku() -> None:
    """
    Vypíše možnosti hlavního menu do konzole.
    """
    print("Správce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")


def pridat_ukol(seznam_ukolu: List[Dict[str, str]]) -> None:
    """
    Umožní uživateli zadat data pro nový úkol a přidá ho do seznamu.
    Provádí validaci, aby vstupy nebyly prázdné.

    Args:
        seznam_ukolu (List[Dict[str, str]]): Seznam, kam se úkol přidá.
    """
    while True:
        nazev_vstup = input("\nZadejte název úkolu: ").strip()
        if not nazev_vstup:
            print("Název úkolu nesmí být prázdný. Zkuste to znovu.")
            continue

        popis_vstup = input("Zadejte popis úkolu: ").strip()
        if not popis_vstup:
            print("Popis úkolu nesmí být prázdný. Zkuste to znovu.")
            continue

        novy_ukol = {"nazev": nazev_vstup, "popis": popis_vstup}
        seznam_ukolu.append(novy_ukol)

        nazev_ukolu = novy_ukol['nazev']
        print(f"Úkol '{nazev_ukolu}' byl přidán.")
        print()
        break


def zobrazit_ukoly(seznam_ukolu: List[Dict[str, str]]) -> None:
    """
    Vypíše všechny úkoly ze seznamu.

    Args:
        seznam_ukolu (List[Dict[str, str]]): Seznam úkolů k zobrazení.
    """
    if not seznam_ukolu:
        print("Seznam úkolů je prázdný.")
    else:
        print("Seznam úkolů:")
        for i, ukol in enumerate(seznam_ukolu, start=1):
            nazev = ukol['nazev']
            popis = ukol['popis']
            print(f"{i}. {nazev} - {popis}")
    
    print()


def odstranit_ukol(seznam_ukolu: List[Dict[str, str]]) -> None:
    """
    Umožní uživateli odstranit úkol ze seznamu podle pořadového čísla.

    Args:
        seznam_ukolu (List[Dict[str, str]]): Seznam, ze kterého se má mazat.
    """
    zobrazit_ukoly(seznam_ukolu)

    if not seznam_ukolu:
        return

    try:
        cislo_ukolu = int(input("Zadejte číslo úkolu, který chcete odstranit: "))

        if 1 <= cislo_ukolu <= len(seznam_ukolu):
            smazany_ukol = seznam_ukolu.pop(cislo_ukolu - 1)
            
            nazev_smazaneho = smazany_ukol['nazev']
            print(f"Úkol '{nazev_smazaneho}' byl odstraněn.")
            print()
        else:
            print("Neplatné číslo úkolu.\n")

    except ValueError:
        print("Chyba: Vstup musí být celé kladné číslo.\n")


def hlavni_menu() -> None:
    """
    Hlavní řídící funkce programu.
    Iniciuje prázdný seznam úkolů a spouští smyčku s menu.
    """
    ukoly: List[Dict[str, str]] = []

    while True:
        zobrazit_nabidku()

        volba = input("Vyberte možnost (1-4): ")

        if volba == '1':
            pridat_ukol(ukoly)

        elif volba == '2':
            print() 
            zobrazit_ukoly(ukoly)

        elif volba == '3':
            print()
            odstranit_ukol(ukoly)

        elif volba == '4':
            print("\nKonec programu.")
            break

        else:
            print("Neplatná volba, prosím zadejte číslo 1-4.\n")


if __name__ == "__main__":
    hlavni_menu()