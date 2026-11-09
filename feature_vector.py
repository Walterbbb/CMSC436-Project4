"""
CMSC 436 Project 4: Build the feature vector
Steps A-H: tokenize, clean, lowercase, remove stop words, stem, count, pick features

Run:  python3 feature_vector.py

A computer can't compare sentences, only numbers. Before we can group similar
movie reviews. This file decides which words get to be columns in that table

We clean the text so different spellings of the same idea count as one word &  throw out words that don't help tell
reviews apart (the, and, etc), and keep only words common enough to matter
"""
import os                          
import re                          
from collections import Counter   
from porter_stemmer import PorterStemmer  

# Data files live in the data/ folder next to this script
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
PARAGRAPHS_FILE = os.path.join(DATA_DIR, "Project4_paragraphs.txt")
STOP_WORDS_FILE = os.path.join(DATA_DIR, "Project4_stop_words.txt")

# T = threshold, A word only makes the feature vector if it appears MORE than T times
# across ALL 52 paragraphs. Raise T -> fewer columns Lower T -> more columns
T = 10


def load_paragraphs(path):
    # The file has one review per line, with blank lines between them & normalizes 
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def load_stop_words(path):
    # checking "word in set" & "word in list" 
    with open(path, encoding="utf-8") as f:
        return {w.strip() for w in f if w.strip()}


def preprocess(paragraph, stop_words, stemmer):
    """Turns one raw paragraph into a clean list of stemmed words."""

    # Remove HTML tags. "<b>movie</b>" -> "movie"
    text = re.sub(r"<[^>]+>", " ", paragraph)

    # Tokenize: split into words on whitespace
    tokens = text.split()

    # Remove punctuation
    tokens = [re.sub(r"[^A-Za-z0-9]", "", t) for t in tokens]

    # Remove numbers
    # Numbers (years, ratings, episode counts)
    tokens = [re.sub(r"[0-9]", "", t) for t in tokens]

    # Some tokens are now empty strings 
    tokens = [t for t in tokens if t]

    # Lowercase everything so "Movie" and "movie" count as the same word
    tokens = [t.lower() for t in tokens]

    # Remove stop words and single-character tokens
    tokens = [t for t in tokens if t not in stop_words and len(t) > 1]

    # takes a string and the start/end indices of the substring to stem
    stems = [stemmer.stem(t, 0, len(t) - 1) for t in tokens]

    # Remove stop words again, because stemming can turn a non-stop word into a stop word
    stems = [s for s in stems if s not in stop_words]
    return stems


def main():
    paragraphs = load_paragraphs(PARAGRAPHS_FILE)
    stop_words = load_stop_words(STOP_WORDS_FILE)
    stemmer = PorterStemmer()  # reused for every word

    # Preprocess every paragraph into a list of stemmed words.
    stemmed = [preprocess(p, stop_words, stemmer) for p in paragraphs]
    # Flatten into ONE big list of every stemmed word in every paragraph
    # (the "list that will contain all stemmed words" the spec asks for)
    all_stems = [w for doc in stemmed for w in doc]

    # Count how many times each stemmed word appears in each paragraph
    per_paragraph = [Counter(doc) for doc in stemmed]
    # total = counts across ALL paragraphs -> used to apply the threshold T
    total = Counter(all_stems)

    # Pick the words that appear more than T times across all paragraphs
    feature_vector = sorted(w for w, c in total.items() if c > T)

    print(f"Paragraphs: {len(paragraphs)}")
    print(f"Total stemmed words: {len(all_stems)}  |  Unique stems: {len(total)}")
    print(f"Threshold T = {T}  ->  feature vector size: {len(feature_vector)}\n")
    print("Feature vector (word: total count):")
    # Print most frequent first 
    for w in sorted(feature_vector, key=lambda w: -total[w]):
        print(f"  {w}: {total[w]}")

    # Returned so Part 2 can do `from feature_vector import main` and reuse
    # everything here instead of re-cleaning the text
    return paragraphs, stemmed, per_paragraph, feature_vector

if __name__ == "__main__":
    main()
