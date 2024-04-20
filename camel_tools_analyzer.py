from camel_tools.tokenizers.word import simple_word_tokenize
from camel_tools.utils.normalize import normalize_unicode, normalize_alef_maksura_ar, normalize_alef_ar, normalize_teh_marbuta_ar

import pandas as pd
from elasticsearch import Elasticsearch

def camel_tools_analyze(text):
    # Normalize the text
    text = normalize_unicode(text)
    text = normalize_alef_ar(text)
    text = normalize_alef_maksura_ar(text)
    text = normalize_teh_marbuta_ar(text)
    
    # Tokenize the text
    tokens = simple_word_tokenize(text)
    
    return ' '.join(tokens)


# Read queries from text file
with open('queries.txt', 'r', encoding='utf-8') as file:
    queries = file.read().splitlines()

def analyze_query(query):
    # Use camel_tools to analyze the query
    tokens = camel_tools_analyze(query)
    return tokens

results = [analyze_query(query) for query in queries]

df = pd.DataFrame({
    'Original Query': queries,
    'Analyzed Query': results
})
df.to_csv('analyzed_queries_camel_tools.csv', index=False, encoding='utf-8-sig')
