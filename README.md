# dfgrzyska.github.io

Strona główna z odnośnikami do moich projektów: https://dfgrzyska.github.io/

Jeden plik `index.html` (style i skrypt w środku), fonty w `fonts/`, zrzuty ekranu w `img/`.
Bez frameworka i bez kroku budowania: GitHub Pages serwuje repo tak, jak jest
(Settings → Pages → *Deploy from a branch* → `main` / `/ (root)`).

## Nowy projekt na liście

1. Skopiuj jeden `<li>` w grupie, do której pasuje projekt („Do własnych spraw” albo „Z ciekawości”,
   każda to osobna `<ol class="projects">`), i zmień link, numer, nazwę, opis (PL i EN) i tagi.
   Numery idą przez obie grupy po kolei.
2. Dodaj zrzut do `img/`:
   - strona na komputer: 960 × 600, `data-kind="desktop"`,
   - apka na telefon: 500 × 900, `data-kind="phone"`.

   `python tools/shots.py <nazwa> <url> desktop|phone` robi zrzut przez Edge w trybie headless.
3. Popraw liczniki: nad całą listą (`06`) i nad grupą (`04`, `02`).

## Lokalnie

```bash
python -m http.server 8080
```
