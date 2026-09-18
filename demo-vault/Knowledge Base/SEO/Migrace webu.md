---
trust-level: approved
---
Postup a zásady při migraci webu na novou strukturu adres. Stránka knowledge base, nikoli projekt; projektové detaily jsou v poznámkách klientů.

## Před migrací

- Crawl produkce jako výchozí stav. Seznam zdrojových adres nikdy jen z crawlu: doplnit adresy ze Search Console a Analytics za 12 měsíců, jinak chybí to, na co nevede interní odkaz.
- Pravidla přesměrování odvozovat po skupinách (kategorie, produkty, články), ne po jednotlivých adresách. Obecné pravidlo plus seznam výjimek.
- Testovací verze musí mít přesměrování nasazené, jinak se nedá ověřit nic.

## Adresy s parametry

Adresy s parametry filtrů, které mají kliky z vyhledávání, přesměrovat na nadřazenou kategorii. Ty bez kliků nechat na kanonizaci nového webu; přesměrování tisíců adres bez hodnoty jen zatěžuje modul přesměrování. Hranici (aspoň jeden klik za rok) volit podle velikosti webu.

## Po migraci

- První den: přesměrování po skupinách, robots.txt, sitemap, canonical na vzorku adres.
- Týdně do konce druhého měsíce: 404 v Search Console a v logu, indexace nových adres.
- Cíl je návrat na úroveň před migrací, ne růst; růst se řeší až po stabilizaci.

## Související

- [[Zahrada Kroupa]], migrace 2026 (adresy s parametry).
