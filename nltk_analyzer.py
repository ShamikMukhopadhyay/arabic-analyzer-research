import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')

# Read queries from text file
with open('queries.txt', 'r', encoding='utf-8') as file:
    queries = file.read().splitlines()

# Tokenize queries using NLTK
results = [word_tokenize(query) for query in queries]

# Create DataFrame
df = pd.DataFrame({
    'Original Query': queries,
    'Analyzed Query': results
})

# Save DataFrame to CSV
df.to_csv('analyzed_queries_nltk.csv', index=False, encoding='utf-8-sig')

