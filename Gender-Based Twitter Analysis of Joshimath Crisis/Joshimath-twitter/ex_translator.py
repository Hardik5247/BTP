import csv
import pandas as pd
from googletrans import Translator

translator = Translator()
data = pd.read_csv('results/joshimath_complete_en.csv')

def convert(col, start, end):
    for i in range(start, len(col)):
    # for i in range(start, end):
        if not isinstance(col[i], str) or all(ord(c) < 128 for c in col[i]):
            continue
        else:
            col[i] = (translator.translate(col[i], dest='en')).text
            # print(i, " " , col[i])
            print(i)

# convert(data['UserScreenName'])
# convert(data['Text'], 5000, 6000)
convert(data['Embedded_text'], 4500, 6000)

data.to_csv('results/joshimath_complete_en.csv')
