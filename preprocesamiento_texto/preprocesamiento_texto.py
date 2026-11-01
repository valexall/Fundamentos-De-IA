"""Ejemplos de preprocesamiento de texto en español según los slides de la semana 7."""

from __future__ import annotations

import re
from pathlib import Path

import nltk
import spacy
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer


TEXTO = (
    "Me encanta aprender procesamiento de lenguaje natural. "
    "El procesamiento de textos ayuda a que los modelos de inteligencia artificial "
    "comprendan mejor la información."
)


def preparar_recursos() -> None:
    """Descarga los recursos de NLTK usados por esta actividad si faltan."""
    nltk.download("punkt", quiet=True)
    nltk.download("punkt_tab", quiet=True)
    nltk.download("stopwords", quiet=True)


def limpiar_texto(texto: str) -> str:
    """Convierte a minúsculas, elimina URLs, números y caracteres especiales."""
    texto = texto.lower()
    texto = re.sub(r"https?://\S+|www\.\S+", "", texto)
    texto = re.sub(r"[^a-záéíóúüñ\s]", " ", texto)
    return re.sub(r"\s+", " ", texto).strip()


def procesar(texto: str) -> dict[str, object]:
    """Ejecuta tokenización, limpieza, normalización y vectorización."""
    texto_limpio = limpiar_texto(texto)
    tokens_palabra = word_tokenize(texto_limpio, language="spanish")
    tokens_oracion = sent_tokenize(texto, language="spanish")

    palabras_paradas = set(stopwords.words("spanish"))
    tokens_sin_stopwords = [
        token for token in tokens_palabra if token not in palabras_paradas
    ]

    stemmer = SnowballStemmer("spanish")
    stems = [stemmer.stem(token) for token in tokens_sin_stopwords]

    nlp = spacy.load("es_core_news_sm")
    documento = nlp(texto_limpio)
    lemas = [
        token.lemma_
        for token in documento
        if token.is_alpha and not token.is_stop
    ]

    vectorizador = TfidfVectorizer(
        lowercase=True,
        stop_words=list(palabras_paradas),
    )
    matriz_tfidf = vectorizador.fit_transform([texto_limpio])

    return {
        "texto_limpio": texto_limpio,
        "tokens_palabra": tokens_palabra,
        "tokens_oracion": tokens_oracion,
        "tokens_sin_stopwords": tokens_sin_stopwords,
        "stems": stems,
        "lemas": lemas,
        "vocabulario_tfidf": vectorizador.get_feature_names_out().tolist(),
        "matriz_tfidf": matriz_tfidf.toarray(),
    }


def main() -> None:
    preparar_recursos()
    resultados = procesar(TEXTO)

    print("TEXTO ORIGINAL:\n", TEXTO)
    print("\n1. Texto limpio:\n", resultados["texto_limpio"])
    print("\n2. Tokens de palabras:\n", resultados["tokens_palabra"])
    print("\n3. Tokens de oraciones:\n", resultados["tokens_oracion"])
    print("\n4. Sin stopwords:\n", resultados["tokens_sin_stopwords"])
    print("\n5. Stemming:\n", resultados["stems"])
    print("\n6. Lematización:\n", resultados["lemas"])
    print("\n7. Vocabulario TF-IDF:\n", resultados["vocabulario_tfidf"])
    print("\n8. Matriz TF-IDF:\n", resultados["matriz_tfidf"])


if __name__ == "__main__":
    main()
