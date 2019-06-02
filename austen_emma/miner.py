import nltk
nltk.download('book', quiet=True)
from nltk.book import *

class Emma:
    def __init__(self):
        nltk.corpus.gutenberg.fileids()
        emma_row = nltk.corpus.gutenberg.raw('austen-emma.txt')
        print(emma_row[:1302])

