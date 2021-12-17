from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import os

credential = AzureKeyCredential(os.environ.get('Azure_Key_Detector'))
endpoint = os.environ.get('TextAnalyticsClient')

text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

def language_detector():

    text = ''
    while text != 'exit':

        document_to_detect = {
        'id' : 'document_to_detect',
        'text' : input('Please type your text : ')
        }

        language_analysis = text_analytics_client.detect_language(documents=[document_to_detect])
        print(f'Text language is : {language_analysis[0].primary_language.name}')
        print('_________________________________  (type "exit" to leave) \n \n')

        text = document_to_detect['text']
    print('See you soon ;)')
        
language_detector()
