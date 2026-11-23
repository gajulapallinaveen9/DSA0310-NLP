# pip install transformers torch sentencepiece
from transformers import pipeline

translator = pipeline('translation_en_to_fr', model='Helsinki-NLP/opus-mt-en-fr')

texts = ['Hello, how are you today?',
         'Machine translation is very useful.',
         'I love learning natural language processing.']

for t in texts:
    result = translator(t, max_length=100)
    print('EN:', t)
    print('FR:', result[0]['translation_text'])
    print()
