from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

API_KEY = '2ebb13e305eb43fcac9b8a6d972e3663'
ENDPOINT = 'https://sentiment-analytics-project.cognitiveservices.azure.com/'

def client():
    # Authenticate the client
    client = TextAnalyticsClient(
        endpoint=ENDPOINT, 
        credential=AzureKeyCredential(API_KEY))
    return client
