---
status: researched
verdict: 🔴
trust-level: ai-generated
---
## Zadání

Toggl umí jen jeden běžící čas, ale často běží dvě nebo tři sessions Claude Code naráz. Podívat se, jestli existuje měření času, které umí souběh, a jestli by se vyplatilo přejít.

## Verdikt

Nepřecházet. Souběžné sessions řeší skill `/toggl-check` z transkriptů, změna nástroje by rozbila import do plánovacího sešitu a historii od roku 2019.

## Kontext (Claude)

- Nástroje se souběžným měřením existují, ale všechny vyžadují ruční start a stop každé úlohy zvlášť, což je víc práce než dnes.
- Toggl je napojený přes Apps Script do Google Sheets, odkud čte plán vs. skutečnost. Každá náhrada by potřebovala nový import.
- Skutečný problém není nástroj, ale to, že souběžná práce se do lineárního záznamu nevejde. To řeší porovnání s transkripty Claude Code (skill `/toggl-check`), které už běží.

## Doporučení (Claude)

- Nechat Toggl. Skill `/toggl-check` pouštět na konci každého dne, ne jen když je čas.
- Za tři měsíce se podívat, kolik hodin `/toggl-check` doplnil; když bude číslo malé, téma zavřít.
