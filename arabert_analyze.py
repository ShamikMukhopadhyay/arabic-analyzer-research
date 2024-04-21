import pandas as pd
import tensorflow as tf
from transformers import AutoTokenizer, TFAutoModelForMaskedLM

# Load AraBERT tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("aubmindlab/bert-base-arabert")
model = TFAutoModelForMaskedLM.from_pretrained("aubmindlab/bert-base-arabert")

# Read queries from text file
with open('queries.txt', 'r', encoding='utf-8') as file:
    queries = file.read().splitlines()

# Analyze queries using AraBERT
results = []
for query in queries:
    # Tokenize the query
    tokens = tokenizer.tokenize(query)
    # Convert tokens to IDs
    input_ids = tokenizer.encode(query, return_tensors="tf")
    # Forward pass through the model
    outputs = model(input_ids)
    # Get the predicted token
    predicted_token_index = tf.argmax(outputs.logits[0], axis=-1)
    predicted_token = tokenizer.convert_ids_to_tokens(predicted_token_index.numpy())
    # Add the predicted token to results
    results.append(predicted_token)

# Create DataFrame
df = pd.DataFrame({
    'Original Query': queries,
    'Analyzed Query': results
})

# Save DataFrame to CSV
df.to_csv('analyzed_queries_arabert.csv', index=False, encoding='utf-8-sig')
