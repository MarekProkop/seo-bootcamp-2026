---
name: backlog
description: Založí novou položku backlogu a/nebo zpracuje všechny nové položky. Bez argumentu zpracuje položky se `status: new`. S argumentem nejdřív založí novou položku z textu argumentu. Použij, když uživatel řekne "/backlog", „dej do backlogu", „někdy vyzkoušet", „prozkoumat, jestli…".
---

# /backlog: nápady k prozkoumání

Backlog jsou nápady k prozkoumání a věci k vyzkoušení, ne znalosti (ty patří do knowledge base, skill `/kb-zapis`) a ne úkoly (ty patří do poznámek projektů). Složka `Backlog/`, formát a stavy definuje poznámka složky [[Backlog]].

## Chování

**Bez argumentu**: najdi položky se `status: new` a každou zpracuj podle kroků 2 až 4. Když žádná není, řekni to a skonči.

**S argumentem** (`/backlog <text>`): text je nový nápad. Postupuj od kroku 1.

### 1. Kontrola duplicit

1. Prohledej `Backlog/` podle klíčových slov z textu (obsah i názvy souborů).
2. Když existuje položka na stejné téma:
   - nový text nepřidává nic navíc → odkaž na ni a skonči;
   - nový text přidává nový úhel nebo otázku → doplň ho do jejího `## Zadání` a pokračuj krokem 2 nad ní. Nový soubor nezakládej.
3. Když nic nenajdeš, založ soubor `Backlog/YYYYMMDD Krátký název tématu.md` (dnešní datum, název česky, bez teček):

   ```markdown
   ---
   status: new
   verdict:
   trust-level: approved
   ---
   ## Zadání

   <text argumentu, jen lehce učesaný>
   ```

### 2. Rešerše

1. **Vault nejdřív.** Prohledej denní zápisy, `Projekty/`, `Knowledge Base/` a `Backlog/` na klíčová slova a synonyma. Marek má k většině témat něco zapsaného, i když rozptýleně.
2. **Pak internet.** Hledej aktuální informace, u nástrojů ověř, že ještě existují a v jaké verzi.
3. Ber v úvahu Markovu sadu nástrojů (Obsidian, Claude Code, R, DuckDB, Screaming Frog, Google Workspace) a to, že je konzultant na volné noze s omezenou kapacitou. Doporučení, které vyžaduje nový nástroj nebo týden práce, musí za to stát.

### 3. Zápis výsledku

Do položky doplň dvě sekce, každou 3 až 8 odrážek nebo krátkých odstavců, česky, bez vaty:

- `## Kontext (Claude)`: co k tématu už ve vaultu je, co se zjistilo venku, co z toho plyne pro Markovu situaci.
- `## Doporučení (Claude)`: konkrétní další kroky, ideálně první krok na jednu hodinu a na kterém klientovi to vyzkoušet.

Pak **verdikt**, ten se nesmí vynechat:

- Hned za `## Zadání` přidej `## Verdikt`: jedna věta, jestli se tím zabývat a proč.
- Do vlastnosti `verdict` zapiš jednu ze tří značek: 🟢 udělat, má hodnotu nebo to spěchá; 🟡 možná, hodnota je, ale nespěchá; 🔴 nechat být, nestojí to za čas.
- Změň `status: new` na `status: researched`. Obsah `## Zadání` nikdy neměň, jen doplňuj.
- Po uložení soubor znovu přečti a ověř, že `verdict` není prázdný. Semafor je to, podle čeho se Marek v přehledu backlogu rozhoduje; položka bez něj vypadá nezpracovaně.

### 4. Hlášení

Jednou větou za položku: název, hlavní závěr, doporučený první krok.

## Poučení

- Rešerše bez prohledání vaultu vedla k doporučením, která už Marek zkoušel a zavrhl. Vault nejdřív, vždy.
- Položka se `status: researched` a prázdným `## Doporučení (Claude)` je horší než položka `new`: vypadá hotově. Sekci doplnit vždy, i kdyby zněla „nedělat, protože…".
- Verdikt se vynechával nejčastěji: model napsal kontext i doporučení a `verdict` nechal prázdný. Proto krok s kontrolou po uložení.
