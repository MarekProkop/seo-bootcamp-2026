---
name: meeting-prep
description: Připraví sekce pro dnešní klientské schůzky do denní poznámky podle Google Kalendáře a historie předchozích schůzek. Use when user says "meeting prep", "příprava schůzek", "připrav schůzky", or "/meeting-prep".
---

# meeting-prep: příprava schůzek do denní poznámky

Zkrácená ukázka skutečného skillu. Postup je stejný, vynechané jsou detaily formátování a chybové stavy.

## Krok 1: Dnešní schůzky z kalendáře

1. Dnešní datum vezmi z kontextu.
2. Načti dnešní události **s účastníky a popisem**, ne jen s názvem a časem:

   ```
   gws calendar events list --params '{"calendarId":"primary","timeMin":"YYYY-MM-DDT00:00:00+02:00","timeMax":"YYYY-MM-DDT23:59:59+02:00","singleEvents":true,"orderBy":"startTime"}' --format json
   ```

3. Z výsledků vezmi název, čas, `attendees[].email`, `attendees[].displayName`, `organizer` a `description`.

## Krok 2: Urči klienta a pravidelnost

**Klienta urči z účastníků a projektů, ne z názvu události.** V tomto pořadí:

- domény v `attendees[].email` a `displayName`,
- projekty: naparuj doménu, jméno nebo téma na složku v `Projekty/`, na fakta v poznámce složky a na zpětné odkazy (`obsidian backlinks file="Klient" format=json`),
- CRM (`CRM/People`, `CRM/Companies`) jako doplněk.

Název události a pole „místo" ber jen jako vodítko. Když událost nejde jednoznačně přiřadit, **zeptej se**, nehádej. Proč: sekce Poučení na konci.

**Pravidelná schůzka** = existuje aspoň jedna předchozí schůzka v denních zápisech (zpětné odkazy na klienta filtrované na `daily/`). **Nepravidelná** = žádná; u té se zeptej, jestli sekci vůbec připravit, a když ano, udělej jen kostru s Agendou a Poznámkami.

## Krok 3: Přečti minulou schůzku

Z denní poznámky nejnovějšího data před dneškem vezmi sekci `## [[Klient]]: …` a vytáhni z ní:

- **Nadpis** doslova.
- **Přítomni**, pokud řádek existuje.
- **Strukturu Výsledků**: domény, metriky, čísla z minula jako „minule X %", nové hodnoty jako `... %`.
- **Otevřené body z Poznámek**: „do příště", rozpracované věci, co kdo slíbil.

## Krok 4: Doplň z projektu, denních zápisů a pošty

- Z poznámky složky projektu `## Aktuální stav` (jedna věta) a otevřené úkoly, které se schůzky týkají (`📋 z projektu`).
- **Cizí úkoly** se štítkem `#watch` ze sekce `## Cizí úkoly`: všechny otevřené, u kterých začalo připomínání (bez `🛫`, nebo s `🛫` dneškem a dřív). Zachovej jméno toho, kdo je má udělat, označ `👀 cizí úkol`.
- Zmínky klienta v denních zápisech od minulé schůzky (`📅 z daily notes`).
- E-maily s klientem od minulé schůzky přes `gws gmail`, filtr podle domény klienta (`✉️ z e-mailu`).

## Krok 5: Sekce do denní poznámky

```markdown
## [[Klient]]: <nadpis z minulé schůzky>

Přítomni: <pokud bylo>

### Hotové úkoly

` ` `tasks
done on or after <datum minulé schůzky> and on or before <dnes>
path includes <Klient>
` ` `

### Agenda

- Aktuální stav projektu: <věta z poznámky složky>
- Výsledky:
	- <struktura z minula>
- <otevřený úkol z projektu> 📋 z projektu
- <cizí úkol> 👀 cizí úkol
- <bod z denních zápisů> 📅 z daily notes
- <bod z e-mailu> ✉️ z e-mailu
- <otevřený bod z minula> ⬅️ z minulé schůzky

### Poznámky, úkoly

```

Podsekce vždy H3, název poslední sekce vždy „Poznámky, úkoly". Sekce připoj na konec dnešní denní poznámky, oddělené `---`. Když denní poznámka neexistuje, založ ji přes `obsidian create`.

## Krok 6: Shrnutí

Vypiš připravené schůzky, u každé datum minulé schůzky a počet převzatých bodů. Připomeň doplnit čísla do Výsledků.

## Poučení: proč se klient určuje z účastníků

Při prvním běhu týdenního plánu (2026-06-08) skončily 4 z 9 schůzek u špatného klienta, protože se klient odvozoval z názvu události: „SEO – quick update" padlo na jiného klienta kvůli textu v poli „místo", „Marek Prokop AI" skončilo jako osobní blok místo nové poptávky, „[Klient] …" se napasovalo na konvenci bloků soustředěné práce místo skutečné schůzky. Účastníci a jejich domény se nemýlí; názvy událostí píší klienti.
