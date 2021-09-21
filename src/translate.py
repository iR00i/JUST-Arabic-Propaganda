import boto3
import pandas as pd
from tqdm import tqdm
import time

train = pd.read_csv('../data/train.csv')
dev = pd.read_csv('../data/dev.csv')

train.sort_values(by=['id'], inplace=True)
train.sort_values(by=['id'], inplace=True)

client = boto3.client('translate')


arabics = pd.DataFrame(columns = ['Arabic', 'id'])
for idx, row in tqdm(train.iterrows(), total = len(train), desc='translating train...'):
    text = train.text_span[idx]
    arabic_text = client.translate_text(Text = text, SourceLanguageCode = 'en', TargetLanguageCode='ar')['TranslatedText']
    arabics = arabics.append({'Arabic': arabic_text, 'id': train.id[idx]}, ignore_index = True)
    arabics.to_csv('../data/train_translated.csv', index = False)
    time.sleep(50/1000)

arabics = pd.read_csv('../data/train_translated.csv')
train['Arabic'] = arabics.Arabic.values
train.to_csv('../data/train_translated.csv', index=False)

arabics = pd.DataFrame(columns = ['Arabic', 'id'])
for idx, row in tqdm(dev.iterrows(), total = len(dev), desc='translating dev...'):
    text = dev.text_span[idx]
    arabic_text = client.translate_text(Text = text, SourceLanguageCode = 'en', TargetLanguageCode='ar')['TranslatedText']
    arabics = arabics.append({'Arabic': arabic_text, 'id': dev.id[idx]}, ignore_index = True)
    arabics.to_csv('../data/dev_translated.csv', index = False)
    time.sleep(50/1000)
    
dev['Arabic'] = arabics.Arabic.values
dev.to_csv('../data/dev_translated.csv', index=False)

print("Done.")