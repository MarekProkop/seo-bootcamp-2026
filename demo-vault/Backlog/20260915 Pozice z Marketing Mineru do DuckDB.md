---
status: researched
trust-level: ai-generated
---
## Zadání

Zkusit stahovat týdenní pozice sledovaných slov z Marketing Mineru do DuckDB, aby šly spojit s crawlem a se Search Console v jednom dotazu. Zatím se pozice čtou jen v rozhraní.

## Kontext (Claude)

- Marketing Miner MCP vrací pozice po dotazech s limitem řádků na volání; pro sto slov jde o jedno volání týdně.
- DuckDB umí číst JSON přímo, stačí ukládat odpovědi do složky a číst je globem.
- Spojení se Search Console je přes dotaz a stránku, s crawlem přes adresu.

## Doporučení (Claude)

Vyzkoušet na [[Bicyklo]] po nasazení nové struktury kategorií: sto slov, jeden týdenní běh na serveru, tabulka `pozice` vedle tabulek z crawlu. Když se osvědčí, udělat z toho skill.
