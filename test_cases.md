# Testovací případy: Task Manager

## Funkce: `hlavni_menu`

**TC01: Výběr platné možnosti z menu (Pozitivní test)**
* **Popis:** Ověření, že volba čísla 1 v hlavním menu správně spustí funkci pro přidání úkolu.
* **Vstupní podmínky:** Program je spuštěn, seznam úkolů je prázdný, zobrazuje se hlavní menu.
* **Kroky testu:** 1. Zadejte číslo `1`. 2. Potvrďte stisknutím klávesy Enter.
* **Očekávaný výsledek:** Program spustí funkci `pridat_ukol()` a vyzve k zadání názvu úkolu.
* **Skutečný výsledek:** Zobrazila se výzva "Zadejte název úkolu:".
* **Stav:** Pass
* **Poznámky:** Základní ověření navigace v programu.

**TC02: Zadání neplatné volby (Negativní test)**
* **Popis:** Ověření reakce programu na zadání čísla mimo rozsah 1-4.
* **Vstupní podmínky:** Program zobrazuje hlavní menu.
* **Kroky testu:** 1. Zadejte číslo `5`. 2. Potvrďte stisknutím klávesy Enter.
* **Očekávaný výsledek:** Program upozorní na neplatnou volbu a znovu zobrazí menu.
* **Skutečný výsledek:** Program vypsal "Neplatná volba, prosím zadejte číslo 1-4." a vrátil se do menu.
* **Stav:** Pass
* **Poznámky:** Lze rozšířit i o test s textovým vstupem (např. "a"), program reaguje stejně.

---

## Funkce: `pridat_ukol`

**TC03: Přidání prvního úkolu s platnými daty (Pozitivní / Hraniční test)**
* **Popis:** Ověření, že lze přidat úkol do prázdného seznamu.
* **Vstupní podmínky:** Uživatel zvolil možnost 1, seznam úkolů je prázdný.
* **Kroky testu:** 1. Do názvu zadejte `Nákup`. 2. Do popisu zadejte `Koupit chleba`.
* **Očekávaný výsledek:** Úkol se uloží do seznamu, program vypíše potvrzení a vrátí se do menu.
* **Skutečný výsledek:** Program vypsal "Úkol 'Nákup' byl přidán." a zobrazil menu.
* **Stav:** Pass
* **Poznámky:** Přidání prvního prvku je vždy důležitý hraniční případ pro inicializaci seznamu.

**TC04: Přidání úkolu s prázdným názvem (Negativní test)**
* **Popis:** Ověření, že program nedovolí vytvořit úkol bez názvu.
* **Vstupní podmínky:** Uživatel zvolil možnost 1.
* **Kroky testu:** 1. Na výzvu k zadání názvu stiskněte pouze Enter (prázdný vstup).
* **Očekávaný výsledek:** Program upozorní na chybu a vyzve k zadání názvu znovu.
* **Skutečný výsledek:** Zobrazilo se "Název úkolu nesmí být prázdný. Zkuste to znovu." a program čeká na nový vstup.
* **Stav:** Pass
* **Poznámky:** Funkce `strip()` ve zdrojovém kódu úspěšně odchytí i vstup složený pouze z mezer.

---

## Funkce: `zobrazit_ukoly`

**TC05: Zobrazení prázdného seznamu úkolů (Hraniční test)**
* **Popis:** Ověření výpisu v situaci, kdy nebyly přidány žádné úkoly.
* **Vstupní podmínky:** Program běží, nebyly přidány žádné úkoly.
* **Kroky testu:** 1. V hlavním menu zadejte `2` a potvrďte.
* **Očekávaný výsledek:** Program informuje uživatele, že je seznam prázdný.
* **Skutečný výsledek:** Program vypsal "Seznam úkolů je prázdný."
* **Stav:** Pass
* **Poznámky:** Zabraňuje chybám při iteraci nad prázdným listem.

**TC06: Zobrazení seznamu s existujícími úkoly (Pozitivní test)**
* **Popis:** Ověření správného formátování výpisu úkolů.
* **Vstupní podmínky:** V seznamu je alespoň jeden úkol (např. "Nákup" - "Koupit chleba").
* **Kroky testu:** 1. V hlavním menu zadejte `2` a potvrďte.
* **Očekávaný výsledek:** Program vypíše úkoly se správným číslováním, názvem a popisem.
* **Skutečný výsledek:** Program vypsal "1. Nákup - Koupit chleba".
* **Stav:** Pass
* **Poznámky:** Číslování začíná správně od 1, nikoliv od 0.

---

## Funkce: `odstranit_ukol`

**TC07: Odstranění existujícího úkolu (Pozitivní test)**
* **Popis:** Smazání úkolu zadáním jeho platného pořadového čísla.
* **Vstupní podmínky:** V seznamu je právě jeden úkol. Uživatel zvolil možnost 3.
* **Kroky testu:** 1. Na výzvu zadejte `1` a potvrďte.
* **Očekávaný výsledek:** Úkol je smazán, program vypíše potvrzení.
* **Skutečný výsledek:** Program vypsal "Úkol 'Nákup' byl odstraněn."
* **Stav:** Pass
* **Poznámky:** Zároveň jde o hraniční případ (smazání posledního úkolu, seznam zůstane prázdný).

**TC08: Pokus o odstranění neexistujícího úkolu (Negativní test)**
* **Popis:** Zadání čísla úkolu, které je větší než počet položek v seznamu.
* **Vstupní podmínky:** V seznamu je jeden úkol. Uživatel zvolil možnost 3.
* **Kroky testu:** 1. Zadejte číslo `99` a potvrďte.
* **Očekávaný výsledek:** Program upozorní, že číslo je neplatné, a úkol nesmaže.
* **Skutečný výsledek:** Zobrazilo se "Neplatné číslo úkolu."
* **Stav:** Pass
* **Poznámky:** Ochrana proti chybě `IndexError`.

**TC09: Zadání písmene místo čísla při odstraňování (Negativní test)**
* **Popis:** Ověření odolnosti programu proti nesprávnému datovému typu na vstupu.
* **Vstupní podmínky:** V seznamu je jeden úkol. Uživatel zvolil možnost 3.
* **Kroky testu:** 1. Zadejte písmeno `a` a potvrďte.
* **Očekávaný výsledek:** Program nespadne, zachytí chybu a vypíše upozornění.
* **Skutečný výsledek:** Zobrazilo se "Chyba: Vstup musí být celé kladné číslo." a návrat do menu.
* **Stav:** Pass
* **Poznámky:** `try-except` blok pro `ValueError` funguje správně.