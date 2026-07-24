import pandas as pd
import re
from collections import Counter

INPUT_FILE = "datos/resenas_flowapp.csv"

def load_data(path: str) -> pd.DataFrame:
    """
    Carga el dataset y convierte tipos necesarios.
    """
    df = pd.read_csv(path)
    df["fecha"] = pd.to_datetime(df["fecha"])

    return df

def normalize_text(text: str) -> str:
    """
    Normaliza texto para análisis.
    - Convierte a minúsculas.
    - Elimina emojis.
    - Elimina caracteres especiales.
    - Elimina números.
    - Normaliza espacios.
    """
    text = text.casefold()
    text = re.sub(r"[\U00010000-\U0010ffff]", "", text)
    text = re.sub(r"[^a-záéíóúüñ\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia y prepara el dataset.
    """
    # Eliminar duplicados
    df = df.drop_duplicates()

    # Eliminar filas sin texto o rating
    df = df.dropna(subset=["texto", "rating"])

    # Mantener únicamente ratings válidos
    valid_ratings = {"1", "2", "3", "4", "5"}
    df = df[df["rating"].isin(valid_ratings)]

    # Convertir rating a entero y normalizar texto
    df["rating"] = df["rating"].astype(int)
    df["texto"] = df["texto"].apply(normalize_text)

    # Eliminar textos vacíos después de limpiar
    df = df[df["texto"] != ""]

    return df

def most_common_words(df: pd.DataFrame, top_n: int = 10):
    """
    Calcula palabras más frecuentes por rating.
    """
    print("\nPalabras más frecuentes por rating")
    print("=" * 50)

    for rating, group in df.groupby("rating"):

        words = " ".join(group["texto"]).split()
        counter = Counter(words)

        print(f"\nRating: {rating}")
        print("-" * 30)

        for word, count in counter.most_common(top_n):
            print(f"{word:<20} {count}")

def statistical_summary(df: pd.DataFrame):
    """
    Genera resumen estadístico de ratings.
    """
    print("\nResumen estadístico")
    print("=" * 30)

    print(f"Total de reseñas: {len(df)}")
    print(f"Promedio: {df['rating'].mean():.2f}")
    print(f"Mediana : {df['rating'].median()}")

    print("\nDistribución:")
    distribution = df["rating"].value_counts().sort_index()
    distribution.index.name = None
    print(distribution.to_string())

    positive = (df["rating"] >= 4).mean() * 100
    neutral = (df["rating"] == 3).mean() * 100
    negative = (df["rating"] <= 2).mean() * 100

    print("\nClasificación de reseñas:")
    print(f"{'Positivas (4-5):':<20} {positive:.2f}%")
    print(f"{'Neutras (3):':<20} {neutral:.2f}%")
    print(f"{'Negativas (1-2):':<20} {negative:.2f}%")

def main():

    df = load_data(INPUT_FILE)
    df = clean_data(df)

    most_common_words(df)
    statistical_summary(df)


if __name__ == "__main__":
    main()