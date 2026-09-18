---
name: youtube
description: Rozebere video z YouTube. Stáhne přepis, shrne obsah a posoudí, jestli stojí za zhlédnutí. Použití: /youtube <adresa videa>. Spusť i tehdy, když uživatel vloží adresu youtube.com nebo youtu.be bez dalšího komentáře.
---

# /youtube: rozbor videa

Cíl je ušetřit čas: místo hodiny sledování pětiminutové čtení a rozhodnutí, jestli video pustit celé, jen část, nebo vůbec.

## Postup

1. **Bez adresy** skonči hlášením „Použití: `/youtube <adresa videa>`".
2. **Stáhni přepis** jedním příkazem, nic jiného v shellu nespouštěj:

   ```
   py ".claude/skills/youtube/yt-download.py" "<adresa>"
   ```

   Skript uloží `YouTube/yt-transcript-<id videa>.txt`: první čtyři řádky jsou `TITLE`, `CHANNEL`, `DURATION`, `URL`, pak `---` a přepis po řádcích s časem `[MM:SS]`. Když skript selže, nahlas chybu a skonči.
3. **Přečti přepis** nástrojem Read a napiš poznámku `YouTube/<Kanál> - <Název videa>.md` (existující přepiš). Přepis pak smaž.
4. **Nahlas** verdikt a dvě věty, proč.

## Struktura poznámky

```markdown
---
created: YYYY-MM-DD
status: new
verdict: 🟢 | 🟡 | 🔴
trust-level: ai-generated
---
## Verdikt

Zhlédnout celé / Podívat se na části / Přeskočit. Jedna až dvě věty proč.

## Co je v tom pro Marka

Co se týká jeho práce (SEO pro e-shopy, Obsidian, Claude Code, R, DuckDB) a co ne. Konkrétní pasáže s odkazem na čas:
`[12:30](https://www.youtube.com/watch?v=<id>&t=750)`. Na rovinu, bez zdvořilostního obalu.

## Shrnutí

Dva až čtyři odstavce: hlavní myšlenky, závěry, co se dá použít.

## Metadata

- **Titulek:** …
- **Kanál:** …
- **Délka:** …
- **Adresa:** …
```

Verdikt: 🟢 zhlédnout, přímo použitelné; 🟡 části stojí za to; 🔴 přeskočit.

## Poučení

- Přepisy z automatických titulků mají chyby v názvech nástrojů a jménech. Když si model není jistý, napíše to, nedomýšlí.
- Bez odkazů s časem je poznámka k ničemu: Marek se chce podívat na dvě minuty, ne hledat je v hodinovém videu.
