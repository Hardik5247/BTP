import pandas as pd

df = pd.read_csv('results/joshimath_complete_en_ner_gender_sentiment.csv')

df_male = df[df['gender'] == 'male']
df_female = df[df['gender'] == 'female']

df_non_person = df[df['NER'] != 'PERSON']

print("len df : ", len(df.index))
print("len df_male : ", len(df_male.index))
print("len df_female : ", len(df_female.index))
print("len df_non_person : ", len(df_non_person.index))


df_male.to_csv('results/all_male.csv')
df_female.to_csv('results/all_female.csv')
df_non_person.to_csv('results/all_non_person.csv')
