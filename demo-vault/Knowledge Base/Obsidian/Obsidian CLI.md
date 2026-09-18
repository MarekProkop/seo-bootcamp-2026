---
trust-level: ai-generated
---
Příkazová řádka Obsidianu (od verze 1.12) komunikuje s běžící aplikací. Agent ji používá místo přímých zásahů do souborů tam, kde Obsidian umí opravit odkazy.

## Kdy použít

- `obsidian rename` a `obsidian move`: přejmenování a přesun poznámky, odkazy v celém vaultu se opraví samy. 17. 9. 2026: přejmenování opravilo 14 odkazů v denních zápisech.
- `obsidian backlinks file="Název" format=json`: zpětné odkazy včetně aliasů, spolehlivější než hledání `[[Název]]` textem.
- `obsidian delete`: přesune do koše Obsidianu, ne nenávratné smazání.

## Pasti

- `property:set` ořeže hodnotu s `[[wikilinkem]]` na prázdno. Vlastnosti s odkazem editovat přímo ve frontmatteru.
- Destruktivní příkazy vždy s `path=přesná/cesta.md`. Bez cesty se název hledá jako wikilink a může trefit jinou poznámku.
- Na Windows z Git Bashe přes `powershell.exe -Command "obsidian …"`.
