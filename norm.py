import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
import nltk

class TextNormalizer(BaseEstimator, TransformerMixin):
    def fit(self, x, y = None):
        return self
    def transform(self, x, y = None):
        x_copy = x.copy()
        for i in range(len(x_copy)):
            x_copy[i] = x_copy[i].lower()
            x_copy[i] = x_copy[i].replace('\n', ' ')
            x_copy[i] = x_copy[i].replace('\r', ' ')
            x_copy[i] = x_copy[i].strip()
        return x_copy


class WordExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, language, tokenize):
        self.language = language
        self.stopwords = stopwords.words(self.language)
        self.tokenize = tokenize

    def fit(self, x, y=None):
        general_freq = FreqDist()
        for txt in x:
            freq_dist = FreqDist(self.tokenize(txt))
            general_freq.update(freq_dist)
        self.hapaxes = general_freq.hapaxes()
        return self

    def transform(self, x, y=None):
        x_copy = x.copy()
        for i in range(len(x_copy)):
            x_copy[i] = ' '.join([token for token in self.tokenize(x_copy[i])
                                  if token not in self.stopwords and
                                  token not in self.hapaxes])
        return x_copy


class ApplyStemmer(BaseEstimator, TransformerMixin):
    def __init__(self, stemmer, tokenize):
        self.stemmer = stemmer
        self.tokenize = tokenize

    def fit(self, x, y=None):
        return self

    def transform(self, x, y=None):
        x_copy = x.copy()
        for i in range(len(x_copy)):
            x_copy[i] = ' '.join([self.stemmer.stem(token)
                                  for token in self.tokenize(x_copy[i])])
        return x_copy