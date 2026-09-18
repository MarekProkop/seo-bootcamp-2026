# Claude Code a Obsidian jako osobní asistent SEO konzultanta

Materiály k přednášce na [SEO Bootcampu 2026](https://seobootcamp.cz/), pátek 18. 9. 2026, Balónový hotel Radešín.

**Autor:** Marek Prokop, [prokopsw.cz](https://www.prokopsw.cz/)

## Slidy

Online: **<https://marekprokop.github.io/seo-bootcamp-2026/>**

Zdroj: [`docs/slides.md`](docs/slides.md) (Marp).

## Ukázkový vault

Složka [`demo-vault/`](demo-vault/) je Obsidian vault se stejnou strukturou, konvencemi, `CLAUDE.md` a skilly, jaké používám ve skutečném vaultu. **Klient Zahrada Kroupa, jeho lidé, čísla a e-shop jsou smyšlení.** Skutečný vault má 1 590 poznámek a `CLAUDE.md` o 258 řádcích; ukázka je zkrácená tak, aby se dala přečíst za deset minut.

Co v něm je:

- `CLAUDE.md`: pravidla pro Claude Code. Struktura vaultu, konvence, formát denních zápisů a poznámek projektů, Obsidian CLI a jeho pasti, pravidla psaní, pravidla vzniklá z chyb agenta.
- `Projekty/Zahrada Kroupa/`: poznámka složky projektu jako jediný zdroj pravdy (Aktuální stav, Kapacita, Úkoly, Cizí úkoly, Archiv statusů) a podpoznámka k migraci.
- `CRM/`: firmy a lidé, jedna poznámka na entitu.
- `daily/`: denní zápisy, jeden se schůzkou připravenou skillem `meeting-prep`.
- `Knowledge Base/`: tematická stránka a Inbox se zachytávkou, kterou noční běh už zařadil.
- `Backlog/`: položka k vyzkoušení.
- `Briefing.md` a `Scripts/briefing-prompt.md`: ukázka ranního briefingu a zkrácený prompt, kterým ho agent na serveru píše.
- `Úkoly.md`: dotazy pluginu Tasks.
- `.claude/skills/`: skilly `meeting-prep` (zkrácený) a `kb-zapis` (celý).

### Jak si ho vyzkoušet

1. Naklonovat repo a otevřít složku `demo-vault` v Obsidianu jako vault. Pluginy: [Tasks](https://publish.obsidian.md/tasks/), [Folder Notes](https://github.com/LostPaul/obsidian-folder-notes), volitelně Bases (součást Obsidianu).
2. V terminálu:

   ```
   cd demo-vault
   claude
   ```

3. Zkusit například: „Jak jsme na tom se Zahradou Kroupa?", „Zapiš: crawl e-shopu vždy s vypnutým JavaScriptem nejdřív" nebo `/meeting-prep` (ten potřebuje [Google Workspace CLI](https://github.com/googleworkspace/cli) a kalendář, bez nich skončí u prvního kroku).

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
