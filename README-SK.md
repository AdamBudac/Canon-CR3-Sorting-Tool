# Canon CR3 Sorting Tool

English guide here: [README.md](README.md)

Jednoduchý nástroj na triedenie Canon `.CR3` RAW súborov – presunie ich do samostatného priečinka, ak sa vo zvolenom adresári nachádza aj zodpovedajúci `.JPG` náhľadový súbor s rovnakým názvom. Tento postup je vhodný najmä preto, že niektoré `.CR3` súbory sa otvárajú veľmi pomaly, takže je časovo efektívnejšie najskôr vytriediť fotografie podľa rýchlo zobraziteľných `.JPG` náhľadov a následne pomocou tohto nástroja automaticky vytriediť `.CR3` RAWy na ďalší postprocessing.

## Funkcie

- **Interaktívny výber priečinka**: Vyberte priečinok na spracovanie pomocou GUI
- **Automatické triedenie**: Všetky `.CR3` súbory, ku ktorým existuje `.JPG` s rovnakým názvom, budú presunuté do podpriečinka `process`
- **Bezpečné spracovanie**: Súbory sa iba presúvajú, originály sa nemenia ani nemažú
- **Funguje na viacerých platformách**: Windows, macOS aj Linux (vyžaduje Python a Tkinter)

## Požiadavky

- Python 3.13
- Tkinter

## Inštalácia

1. Nainštalujte [Python](https://www.python.org/) 3.13

## Použitie

1. Spustite skript dvojklikom alebo v konzole:

```bash
python cr3sort.py
```

2. Vyberte priečinok, ktorý obsahuje vaše `.CR3` a `.JPG` súbory

## Licencia

Zadarmo
