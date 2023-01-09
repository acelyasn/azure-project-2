import pandas as pd
from itertools import zip_longest
import sys
sys.path.append('Text-Analytics')
from credentials import client
import csv

client = client()

#for iterating the document to divide them into chunks of 10
def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


# Create a CSV file and write the header row
with open('sentiment_scores.csv', 'w', newline='') as csvfile:
    fieldnames = ['text', 'sentiment', 'positive','neutral','negative']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

#getting the first 100 reviews 
df = pd.read_csv("Womens Clothing E-Commerce Reviews.csv")
df_100 = df.head(100)

#creating documents list for azure analyze_sentiment method
documents = []
for index, row in df_100.iterrows():
    documents.append({
        'id': str(index),
        'language': 'en',
        'text': row['Review Text']
    })

#getting the "documents" from the grouper created above, 10 by 10
for documents_batch in grouper(documents, 10):
    documents_batch = [d for d in documents_batch if d is not None]
    response = client.analyze_sentiment(documents=documents_batch,show_opinion_mining=True)
    
    #iterating through the elements of responses and writing all into a .csv file 
    for item in response:
    
        txt = item.sentences[0]['text']
        sent = item.sentences[0]['sentiment']
        pos_confidence = item.sentences[0]['confidence_scores']['positive']
        neg_confidence = item.sentences[0]['confidence_scores']['negative']
        neutral_confidence = item.sentences[0]['confidence_scores']['neutral']
        with open('sentiment_scores.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'text': txt, 'sentiment': sent, 'positive': pos_confidence,
             'neutral' : neutral_confidence, 'negative' : neg_confidence})
        





        



