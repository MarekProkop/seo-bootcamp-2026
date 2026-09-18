---
trust-level: ai-generated
---
Plán migrace kroupa-zahrada.cz na nový e-shop. Projekt: [[Zahrada Kroupa]].

## Termíny

- Testovací verze s přesměrováním: slíbená na týden od 15. 9. ([[Tomáš Vydra]]).
- Den D: 1. 10. 2026, potvrzeno [[Petra Kroupová|Petrou]] na schůzce 10. 9.
- Pomigrační kontroly: 1.–3. 10., pak týdně do konce října.

## Co se mění

- Adresy kategorií z `/kategorie/zahradni-nabytek/` na `/zahradni-nabytek/`.
- Adresy produktů z `/produkt/123-nazev` na `/p/nazev-123`.
- Blog zůstává, ale jen vybrané články (rozhoduje Petra).
- Adresy s parametry filtrů (`?barva=`, `?material=`) na starém webu indexované, na novém mají být kanonizované na kategorii.

## Můj postup

1. Předmigrační crawl produkce (hotovo 3. 9.), seznam zdrojových adres doplněný o adresy z Search Console a Analytics (hotovo 8. 9.).
2. Předmigrační crawl testovací verze, kontrola přesměrování po skupinách adres, odvození dalších pravidel.
3. Den D: kontrola přesměrování produkce, robots, sitemap, canonical.
4. Týdenní sledování 404 a indexace v Search Console do konce října.

## Otevřené

- Co s adresami s parametry: přesměrovat na kategorii, nebo nechat 404? Zatím se kloním k přesměrování u těch, které mají za rok kliky.
