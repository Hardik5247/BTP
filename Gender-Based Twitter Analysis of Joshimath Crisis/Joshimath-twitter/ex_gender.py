import requests
import time
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

from urllib.request import urlopen
import json

df = pd.read_csv('results/joshimath_complete_en_ner_gender.csv')

# df['gender'] = ''

for i in range(4800, len(df['UserScreenName'])):
# for i in range(4800):
    print(i)
    if (isinstance(df['UserScreenName'][i], float) or df['NER'][i] != 'PERSON'):
        continue

    name = ''
    for c in df['UserScreenName'][i]:
        if c != ' ':
            name += c
        else:
            break

    url = "https://api.genderize.io?name="+(name)+"&country_id=IN"

    try:
        res = urlopen(url)
    except Exception as e:
        print(e)
        continue

    res_json = json.loads(res.read())
    df['gender'][i] = res_json['gender']
    print(name)
    print(df['gender'][i])
    # break

df.to_csv('results/joshimath_complete_en_ner_gender.csv')
