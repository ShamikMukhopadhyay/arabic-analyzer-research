import pandas as pd
from elasticsearch import Elasticsearch

# Read queries from text file
with open('queries.txt', 'r', encoding='utf-8') as file:
    queries = file.read().splitlines()

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")

def analyze_query(query):
    body = {
        "analyzer": "arabic",
        "text": query
    }
    result = es.indices.analyze(body=body)
    tokens = [token['token'] for token in result['tokens']]
    return ' '.join(tokens)

results = [analyze_query(query) for query in queries]

df = pd.DataFrame({
    'Original Query': queries,
    'Analyzed Query': results
})
df.to_csv('analyzed_queries_es_analyzer.csv', index=False, encoding='utf-8-sig')
