from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = Path(__file__).parent / "netflix_titles.csv.zip"
df = pd.read_csv(DATA_PATH)

# 1. kérdés : Mely megjelenési évekből származik a legtöbb cím a vizsgált Netflix-adathalmazban?

df["date_added"] = pd.to_datetime(
    df["date_added"].str.strip(),
    errors="coerce"
)

df["year_added"] = df["date_added"].dt.year

titles_added_by_year = (
    df["year_added"]
    .value_counts()
    .sort_index()
)

titles_added_by_year.plot(
    kind="line",
    marker="o",
    figsize=(12, 6)
)

plt.title("A Netflixre felkerült tartalmak száma évenként")
plt.xlabel("Felkerülés éve")
plt.ylabel("Tartalmak száma")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()       

# 2. kérdés : A vizsgált adathalmazban filmekből vagy sorozatokból található több?

type_counts = df["type"].value_counts()

ax = type_counts.plot(
    kind="bar",
    figsize=(8, 5),
    color=["#E50914", "#444444"]
)

plt.title("Filmek és sorozatok száma")
plt.xlabel("Tartalomtípus")
plt.ylabel("Darabszám")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 3. kérdés : Mely gyártási országok szerepelnek a legtöbbször a vizsgált Netflix-adathalmazban?

countries = (
    df["country"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
)

top_countries = countries.value_counts().head(10).sort_values()

top_countries.plot(
    kind="barh",
    figsize=(10, 6),
    color="#E50914"
)

plt.title("A 10 leggyakoribb gyártási ország")
plt.xlabel("Tartalmak száma")
plt.ylabel("Ország")
plt.tight_layout()
plt.show()

# 4. kérdés: Mely műfaji kategóriák fordulnak elő leggyakrabban a vizsgált adathalmazban?

genres = (
    df["listed_in"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
)

top_genres = genres.value_counts().head(10).sort_values()

top_genres.plot(
    kind="barh",
    figsize=(10, 6),
    color="#E50914"
)

plt.title("A 10 leggyakoribb műfaji kategória")
plt.xlabel("Előfordulások száma")
plt.ylabel("Műfaji kategória")
plt.tight_layout()
plt.show()

# 5. kérdés: Hogyan változott a filmek átlagos játékideje a megjelenési év függvényében?

movies = df.loc[df["type"] == "Movie"].copy()

movies["duration_num"] = pd.to_numeric(
    movies["duration"].str.extract(r"(\d+)")[0],
    errors="coerce"
)

movies = movies.dropna(
    subset=["release_year", "duration_num"]
)

avg_duration = (
    movies.groupby("release_year")["duration_num"]
    .mean()
)

avg_duration.plot(
    kind="line",
    figsize=(12, 6),
    color="royalblue",
    linewidth=2
)

plt.title("A filmek átlagos játékidejének változása")
plt.xlabel("Megjelenési év")
plt.ylabel("Átlagos játékidő (perc)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


