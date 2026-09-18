---
trust-level: ai-generated
---
Vstupní brána knowledge base. Sem padají zachytávky: myšlenky, fakta, citáty, postupy. Z Telegramu („Zapiš: …"), z PC (skill `/kb-zapis`) a z web clipperu. Zachytávka je neměnný zdroj: obsah se po uložení needituje, agent při zařazení mění jen frontmatter.

## Formát zachytávky

Název souboru: `YYYYMMDD-HHMM Krátký titulek.md` (bez teček).

```
---
status: new
zdroj: <URL, kniha, video, osoba; nepovinné>
zachyceno: YYYY-MM-DD
kanal: telegram | pc | clipper
---
<text zachytávky, co nejblíž původním slovům>
```

Po zařazení do knowledge base (noční běh na serveru) přibude ve frontmatteru `status: zpracováno`, `zpracovano: YYYY-MM-DD` a `zarazeno:` se seznamem stránek, kam se poznatek propsal.
