---
name: kb-zapis
description: Uloží zachytávku (myšlenku, dílčí znalost, citát, fakt nebo postup) do Knowledge Base/Inbox jako vstup pro knowledge base. Použij, když uživatel řekne "/kb-zapis", „zapiš:", „zapiš si", „poznamenej si" a následuje obsah k zapamatování. Zápis ze schůzky = skill prepis. Nápad k prozkoumání nebo věc k vyzkoušení = skill backlog.
---

# /kb-zapis: zachytávka do knowledge base

Skill uloží text jako zachytávku do `Knowledge Base/Inbox/`. Nic nezařazuje, nerešeršuje, nerozepisuje; zařazení do tematických stránek dělá noční běh na serveru. Formát zachytávky definuje poznámka složky [[Inbox]].

## Postup

1. **Vezmi text** z argumentu, případně z kontextu konverzace („zapiš si tohle"). Zachovej uživatelova slova: drobné učesání překlepů ano, přepisování a rozšiřování ne. Citát ulož i s autorem.
2. **Urči krátký titulek** (3–6 slov, česky, bez teček) a **zdroj**, pokud z textu plyne (URL, kniha, video, osoba). Nevymýšlej ho.
3. **Zapiš soubor** `Knowledge Base/Inbox/YYYYMMDD-HHMM Titulek.md` (datum a čas teď):

   ```
   ---
   status: new
   zdroj: <jen když je znám>
   zachyceno: YYYY-MM-DD
   kanal: pc
   ---
   <text zachytávky>
   ```

4. **Potvrď jednou větou** s odkazem na soubor. Žádné další akce.
