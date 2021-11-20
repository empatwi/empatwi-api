import re
import nltk
import spacy

import pandas as pd
import numpy as np

from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download("punkt")
nltk.download("stopwords")

class PreprocessingRepository():

    nlp = spacy.load("pt_core_news_sm")

    def apply_preprocessing(self, df):
        df_clean_text = df.copy()
        df_clean_text["tweet_content"] = df["tweet_content"].apply(self.preprocessing)
        return df_clean_text

    def preprocessing(self, text):
        custom_stops = ["pra", "q", "_", "vai", "vc", "tá", "gente", "tô", "to", "aqui", "tava",
                   "ta", "tá", "hoje", "hj", "-", "eh", "so", "n", "c", "mó", "modalmais",
                   "ouotison", "tbm", "tão", "aí", "nu", "p", "mano", "nois", "pro", "umas",
                   "uns", "então", "x", "ne", "kkkkkkkk", "kkk", "vou", "vcs", "kkkkk", 
                    "nicole", "kkkk", "vivianlana", "gabriel_geno", "ai", "tou", "vir", "ja", 
                    "já", "pq", "amg", "ti", "onde", "meio", "outro", "amigo", "sep_bella",
                   "_gabriel_geno_", "manu", "ir", "tt", "mim", "psg", "sep_bella_", "s",
                   "tudo", "todo", "todos", "rodrigobuenotv", "limite", "aumentar", "querer", 
                    "fazer", "querer", "comprar", "ser", "nathalia", "mt", "en", "d"]
        lower_text = text.lower()
        letters = re.findall(r"\b[A-zÀ-úü]+\b", lower_text)

        stops = set(stopwords.words("portuguese")) 
        without_stopwords = [w for w in letters if 
                                w not in stops and 
                                w not in custom_stops]
        important_words = " ".join(without_stopwords)

        spc_letras = self.nlp(important_words)
        lemmas = [token.lemma_ if token.pos_ == "VERB" else str(token) for token in spc_letras]
        clean_text = " ".join(lemmas)

        print(f'Clean tweet: {clean_text}')
        return clean_text
        