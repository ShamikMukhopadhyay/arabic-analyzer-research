import pandas as pd
import spacy

# Load spaCy Arabic model
nlp = spacy.load("xx_ent_wiki_sm")

# Read queries from text file
with open('queries.txt', 'r', encoding='utf-8') as file:
    queries = file.read().splitlines()

# Analyze queries using spaCy
results = []
for query in queries:
    doc = nlp(query)
    analyzed_query = " ".join([token.text for token in doc])
    results.append(analyzed_query)

# Create DataFrame
df = pd.DataFrame({
    'Original Query': queries,
    'Analyzed Query': results
})

# Save DataFrame to CSV
df.to_csv('analyzed_queries_spacy.csv', index=False, encoding='utf-8-sig')

