# CLAUDE.md

Pokyny pro Claude Code v tomhle vaultu. Ukázková, zkrácená verze skutečného souboru (ten má 258 řádků); struktura a typ pravidel jsou stejné, klient je smyšlený.

## Co to je

Osobní Obsidian vault SEO konzultanta. Slouží jako znalostní báze, CRM, evidence projektů a archiv textů. Obsah je česky.

## Struktura

- **Projekty/**: jedna složka na klienta, poznámka složky se stejným názvem je jediný zdroj pravdy o projektu.
- **CRM/People/** a **CRM/Companies/**: kontakty. Každá osoba a firma má právě jednu poznámku.
- **Knowledge Base/**: tematické stránky (SEO, DuckDB, Obsidian…). `Knowledge Base/Inbox/` je vstup pro zachytávky.
- **daily/**: denní zápisy `YYYY-MM-DD.md`.
- **Backlog/**: nápady k prozkoumání a věci k vyzkoušení, `YYYYMMDD Téma.md`, vlastnost `status`.
- **Scripts/**: prompty pro automatizace (ranní briefing, noční zařazení).
- **templates/**: šablony Obsidianu.
- **Úkoly.md**: dotazy Tasks pluginu, žádné vlastní úkoly.

## Konvence

- **Wikilinky všude.** Každá zmínka osoby, firmy, projektu nebo tématu je `[[wikilink]]`. Když poznámka neexistuje, založ ji (osoba ze šablony `People`, firma s `tag: company`).
- **Název firmy = plný právní název** včetně právní formy (`KROUPA zahrada s.r.o.`). Značku přidej do `aliases:`.
- **Žádné H1 v poznámkách.** Název poznámky je název souboru. Tělo začíná textem nebo `##`.
- **Žádné tečky v názvech souborů a složek**, výjimka je právní forma firmy.
- **Vše, co napíšeš, dostane `trust-level: ai-generated`** ve frontmatteru. Na `approved` to mění jen Marek, nikdy ty. Jiné hodnoty neexistují.
- **Vytvořeno (➕) u úkolu je datum, kdy úkol skutečně vznikl** (dohoda na schůzce, slib), ne kdy ho zapisuješ.

## Denní zápisy

Dva druhy záznamů podle velikosti:

1. **Malý záznam**: jeden odstavec. Začíná `[[wikilinkem]]` na téma nebo projekt, dvojtečkou a obsahem. `[[Zahrada Kroupa]]: Petra potvrdila den D migrace na 1. 10.`
2. **Velký záznam** (schůzka, delší update): nadpis `## [[Projekt]]: krátký titulek`, pod ním odstavce, odrážky, podnadpisy od H3 níž.

Společné: osoby v těle vždy jako `[[Jméno]]`. Odrážky jsou věty a končí tečkou. Každý řádek musí dávat smysl za měsíc bez kontextu konverzace. Nové sekce vždy na konec souboru. Záznamy v rámci dne odděluj `---` s prázdným řádkem nad ním.

## Poznámky projektů

Poznámka složky projektu je jediný zdroj pravdy. Stavy, fakta a historie žijí tady, ne v denních zápisech a ne v tvé paměti.

```markdown
krátký úvod (1–3 věty, co projekt je)

## Aktuální stav
YYYY-MM-DD: jedna věta s wikilinkem na detail

## Kapacita
N h měsíčně

## Úkoly            (dotaz Tasks + „### Úkoly, zdroj")
## Cizí úkoly       (dotaz Tasks + „### Cizí úkoly, zdroj")
… další sekce projektu …

## Archiv statusů
YYYY-MM-DD: starší stav
```

- **`## Aktuální stav` je přesně jedna věta.** Detaily a čísla patří do dedikovaných poznámek v projektu, status na ně odkazuje.
- **Při změně stavu** přesuň dosavadní blok beze změny na začátek `## Archiv statusů` a na jeho místo napiš nový.
- **Nová fakta zapracuj do existujících sekcí.** Žádná sekce „Závěry ze schůzky YYYY-MM-DD".
- **Před plánováním hodin vždy přečti `## Kapacita`.** Nespoléhej na zapamatované číslo.

## Cizí úkoly (`#watch`)

Úkoly, které má udělat někdo jiný, ale Marek je hlídá. Formát `- [ ] [[Kdo]]: co má udělat. #watch ➕ YYYY-MM-DD`. Bez termínu 📅 (druhá strana ho neslíbila). Zavírání `[x]` udělali, `[-]` přestalo být potřeba. Nemíchat s Markovými úkoly.

## Obsidian CLI

Pro přesuny, přejmenování, mazání a vlastnosti používej `obsidian` CLI, ne přímé zásahy do souborů: `obsidian move`, `obsidian rename` (opraví wikilinky), `obsidian delete` (do koše Obsidianu), `obsidian property:set`, `obsidian backlinks file="Název" format=json`.

- Na Windows z Git Bashe přes `powershell.exe -Command "obsidian …"`.
- **`property:set` tiše ořeže `[[wikilinky]]`.** Vlastnosti s wikilinkem edituj přímo ve frontmatteru.
- **Destruktivní operace vždy s `path=přesná/cesta.md`**, nikdy pozičně. Fuzzy hledání jednou trefilo jiný soubor.
- **Nikdy hromadně needituj soubory vaultu skriptem.** Hromadný přepis PowerShellem vymazal 41 poznámek na 0 bajtů (2026-03-29). Pro víc souborů smyčka `property:set`, pro obsah nástroj Edit po jednom souboru.

## Nepřidávej, co jsem nechtěl

Sloupec, sekce, interaktivita, příklad, kontrola „pro jistotu": nic z toho bez vyžádání. Rozsah zadání je zadání. Když si myslíš, že něco chybí, napiš to jednou větou a počkej na odpověď. (Pokyn Marka, 17. 8. 2026, po rozboru logů, opakovalo se to v pěti projektech.)

## Paměť

Automatickou paměť Claude Code nepoužívej: nezapisuj do ní ani z ní nečti. Trvalé znalosti patří sem nebo do poznámky projektu, kde je Marek vidí a může je opravit.

## Psaní česky

- Bez anglicismů, kde má čeština vlastní slovo: odrážky, úkoly, paušál, termín, schůzka.
- Žádné vymyšlené termíny. Když si nejsi jistý, popiš věc obyčejně.
- Pomlčky výjimečně, a když, tak česká (–), nikdy dlouhá (—).
- Odrážky začínající velkým písmenem končí tečkou.
- Obsidian note = **poznámka**, nikdy „nota".
- Nevymýšlej čísla, citace ani reference. Když data nejsou, řekni to.

## Fakturoid MCP

Pro obrat u vystavených faktur: hodnota je cena bez DPH (`native_subtotal`, ne `subtotal`), rozhodující datum je datum zdanitelného plnění (`taxable_fulfillment_due`), ne `issued_on`. Vždy `action=show` u každé faktury, `index` vrací jen cenu s DPH. Žádné odhady typu `native_total / 1,21`. Toggl není zdroj obratu.

## Plánování kapacity

Než řekneš, kolik je volné kapacity, projdi všechny čtyři zdroje: nabídnutou nepotvrzenou kapacitu (denní zápisy se štítkem `#planovani-kapacity`), plán na další měsíce v Google Sheets, `## Aktuální stav` aktivních projektů a skutečné plnění posledních měsíců. Nepočítej s plánovaným číslem tam, kde ho klient měsíce nenaplňuje.
