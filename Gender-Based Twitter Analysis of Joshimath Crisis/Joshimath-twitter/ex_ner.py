import pandas as pd
import spacy

nlp = spacy.load('en_core_web_trf')

df = pd.read_csv('results/joshimath_complete_en.csv')

df['NER'] = ''

for i in range(len(df['UserScreenName'])):
    print("\n",i)
    if isinstance(df['UserScreenName'][i], float):
        continue

    doc = nlp(df['UserScreenName'][i], disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])
    # df['NER'][i] = doc.ents.label_
    for ent in doc.ents:
        df['NER'][i] = ent.label_
        print(ent.label_)

df.to_csv('results/joshimath_complete_en_ner.csv')
