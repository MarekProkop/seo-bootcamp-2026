---
status: researched
verdict: 🟡
trust-level: ai-generated
---
## Zadání

Vyzkoušet, jestli se dá při crawlu e-shopu vytáhnout cena a dostupnost produktu přes custom extraction (CSSPath), aby šlo v DuckDB spojit organickou návštěvnost s cenovou hladinou. První kandidát [[Zahrada Kroupa]] po migraci.

## Verdikt

Má smysl, ale až po migraci Zahrady Kroupa: na starém webu se cena vykresluje skriptem a crawl bez JavaScriptu ji nevidí.

## Kontext (Claude)

- Screaming Frog umí custom extraction přes CSSPath, XPath i regulární výraz; výstup je sloupec v exportu `internal_html`, takže do DuckDB jde bez další práce.
- Na kroupa-zahrada.cz se cena doplňuje skriptem po načtení stránky. Bez vykreslování JavaScriptu bude sloupec prázdný, s vykreslováním se crawl zpomalí zhruba pětkrát.
- Nový e-shop (den D 1. 10.) podle testovací verze cenu vypisuje přímo v HTML, tam to půjde bez JavaScriptu.
- Ve vaultu k tomu nic dřívějšího není.

## Doporučení (Claude)

- Počkat na migraci, pak jeden zkušební crawl kategorie zahradního nábytku (zhruba 300 produktů) s extrakcí ceny a dostupnosti.
- V DuckDB spojit s kliky ze Search Console přes adresu a podívat se, jestli produkty bez skladu berou kliky, které by mohly jít jinam.
- Když to dá smysl, přidat extrakci do profilu crawlu klienta v repu, ne do obecné metodiky.
