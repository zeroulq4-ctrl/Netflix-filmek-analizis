# Netflix-filmek és sorozatok adatelemzése

## A projekt bemutatása

Ez a projekt a Netflix-filmeket és -sorozatokat tartalmazó adathalmaz egyszerű, feltáró elemzését mutatja be Python használatával.


## Vizsgált kérdések

A program a következő kérdéseket vizsgálja:

1. Hogyan változott a Netflixre felkerülő tartalmak száma az évek során?
2. Filmekből vagy sorozatokból található több az adathalmazban?
3. Mely gyártási országok szerepelnek a legtöbbször?
4. Mely műfaji kategóriák fordulnak elő leggyakrabban?
5. Hogyan változott a filmek átlagos játékideje a megjelenési év függvényében?


## Felhasznált technológiák

- Python 3
- Pandas
- Matplotlib


## A projekt felépítése

```text
netflix-data-analysis/
├── netflix movies.py
├── netflix_titles.csv.zip
├── README.md
├── .gitignore
```


## Telepítés és futtatás

### 1. A repository letöltése

```bash
git clone https://github.com/zeroulq4-ctrl/Netflix-filmek-analizis.git
cd netflix-data-analysis
```


### 2. Virtuális környezet létrehozása

Windows alatt:

```bash
py -m venv .venv
.venv\Scripts\activate
```

Linux vagy macOS alatt:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. A szükséges csomagok telepítése

```bash
python -m pip install -r requirements.txt
```

### 4. A program futtatása

```bash
python netflix_analysis.py
```

Windows alatt szükség esetén:

```bash
py netflix_analysis.py
```

## Az adatok kezelése

A program a projekt mappájában található `netflix_titles.csv.zip` fájlt olvassa be. Emiatt nincs szükség a saját számítógépre mutató abszolút fájlútvonal megadására.

Példa a fájl hordozható betöltésére:

```python
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).parent / "netflix_titles.csv.zip"
df = pd.read_csv(DATA_PATH)
```

Az elemzés során a program többek között:

- megszámolja a különböző tartalomtípusokat;
- felbontja a több országot tartalmazó mezőket;
- felbontja a több műfajt tartalmazó mezőket;
- számmá alakítja a filmek percben megadott játékidejét;
- csoportosítja az adatokat megjelenési év szerint;
- diagramokon jeleníti meg az eredményeket.

## Fontosabb megfigyelések

A program futtatása után ide kerülhetnek a konkrét eredmények. Például:

- A vizsgált adathalmazban a filmek száma nagyobb vagy kisebb a sorozatok számánál.
- A legtöbbször előforduló gyártási ország: **Amerika**.
- A leggyakoribb műfaji kategória: **Drama**.
Ezeket a mondatokat a program által kiírt eredmények és diagramok alapján kell kitölteni.

## Korlátok

- Az eredmények csak a felhasznált adathalmaz rekordjaira érvényesek.
- Az adathalmaz nem feltétlenül tartalmazza a Netflix teljes vagy aktuális kínálatát.
- Egy tartalomhoz több ország és több műfaji kategória is tartozhat.
- A régebbi megjelenési évekhez kevés film tartozhat, ezért az ezekből számított átlagok kevésbé megbízhatók.
- A megjelenési év és a Netflixre való felkerülés éve nem ugyanaz az adat.
- Egy szórásdiagramon látható kapcsolat vagy korreláció önmagában nem bizonyít ok-okozati összefüggést.

## Adatforrás

Az adathalmaz forrása: **https://www.kaggle.com/code/aryantiwari123/netflix-movies-and-tv-shows**.



## Készítő

Horváth Máté Gábor
