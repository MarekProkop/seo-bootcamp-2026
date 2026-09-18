# Claude Code a Obsidian jako osobní asistent SEO konzultanta

Materiály k přednášce na [SEO Bootcampu 2026](https://seobootcamp.cz/), pátek 18. 9. 2026, Balónový hotel Radešín.

**Autor:** Marek Prokop, [prokopsw.cz](https://www.prokopsw.cz/)

## Slidy

Online: **<https://marekprokop.github.io/seo-bootcamp-2026/>**

Zdroj: [`docs/slides.md`](docs/slides.md) (Marp).

## Ukázkový vault

Složka [`demo-vault/`](demo-vault/) je Obsidian vault se stejnou strukturou, konvencemi, `CLAUDE.md` a skilly, jaké používám ve skutečném vaultu. **Všichni klienti, jejich lidé, weby a čísla jsou smyšlení.** Skutečný vault má 1 590 poznámek a `CLAUDE.md` o 258 řádcích; ukázka je zkrácená tak, aby se dala přečíst za deset minut.

Co v něm je:

- `CLAUDE.md`: pravidla pro Claude Code. Struktura vaultu, konvence, formát denních zápisů a poznámek projektů, Obsidian CLI a jeho pasti, pravidla psaní, pravidla vzniklá z chyb agenta.
- `Projekty/`: tři smyšlení klienti (Zahrada Kroupa, Bicyklo, Penzion Hvězda). Poznámka složky každého projektu jako jediný zdroj pravdy (Aktuální stav, Kapacita, Úkoly, Cizí úkoly, Archiv statusů) a podpoznámka s detailem.
- `Nabídky.md`: poptávka, která ještě není projekt.
- `CRM/`: firmy a lidé, jedna poznámka na entitu.
- `daily/`: šest denních zápisů, dvě schůzky připravené skillem `meeting-prep`.
- `Knowledge Base/`: tematické stránky a Inbox se zachytávkami.
- `Backlog/`: položky k vyzkoušení a tabulka Bases.
- `Briefing.md` a `Scripts/briefing-prompt.md`: ukázka ranního briefingu a zkrácený prompt, kterým ho agent na serveru píše.
- `Úkoly.md`: dotazy pluginu Tasks.
- `.claude/skills/`: skilly `meeting-prep` (zkrácený) a `kb-zapis` (celý).
- `.obsidian/`: nastavení vaultu a doplňky Tasks a Folder Notes, aby šel otevřít bez instalace.

### Jak si ho vyzkoušet

1. Naklonovat repo a otevřít složku `demo-vault` v Obsidianu jako vault. Doplňky [Tasks](https://publish.obsidian.md/tasks/) a [Folder Notes](https://github.com/LostPaul/obsidian-folder-notes) jsou přibalené, Obsidian se jen zeptá, jestli je smí zapnout.
2. V terminálu:

   ```
   cd demo-vault
   claude
   ```

3. Zkusit například: „Jak jsme na tom s Bicyklem?", „Zapiš: crawl e-shopu vždy s vypnutým JavaScriptem nejdřív" nebo `/meeting-prep` (ten potřebuje [Google Workspace CLI](https://github.com/googleworkspace/cli) a kalendář, bez nich skončí u prvního kroku).

## Co je potřeba mít nainstalované

- [Obsidian](https://obsidian.md/) 1.12 nebo novější (kvůli příkazové řádce `obsidian`).
- [Claude Code](https://docs.claude.com/en/docs/claude-code).
- Node.js jen pro lokální náhled a sestavení slidů.

## Lokální náhled slidů

```
npm install
npm run preview
```

`npm run build` vygeneruje `docs/index.html`, ze kterého běží GitHub Pages.
