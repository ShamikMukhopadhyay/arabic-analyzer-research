from arabicnlp import ArabicNLP
import pandas as pd

# Initialize ArabicNLP analyzer
analyzer = ArabicNLP()

# Read queries from text file
with open('queries.txt', 'r', encoding='utf-8') as file:
    queries = file.read().splitlines()

# Analyze queries using ArabicNLP
results = [analyzer.analyze(query) for query in queries]

# Create DataFrame
df = pd.DataFrame({
    'Original Query': queries,
    'Analyzed Query': results
})

# Save DataFrame to CSV
df.to_csv('analyzed_queries_arabicnlp.csv', index=False, encoding='utf-8-sig')
