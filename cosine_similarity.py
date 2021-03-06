# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hGrQxUAKA5w_jmHFm9H_jm-lhSntQeVf

#COSINE_SIMILARITY

#IMPORTING THE LIBRARIES
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""#PRINTING COUNT MATRIX AND CONVERTING IT TO ARRAY"""

text = ["London Paris London","Paris Paris London"]
cv = CountVectorizer()
count_matrix = cv.fit_transform(text)
print(count_matrix)
print(count_matrix.toarray())

"""#PRINTING THE SIMILARITY SCORES USING COSINE SIMILARITY"""

similarity_scores = cosine_similarity(count_matrix)
print (similarity_scores)