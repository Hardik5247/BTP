import csv
import pandas as pd


# data = pd.read_csv('.\outputs\joshimath_word_en_ner_test_gender_scores.csv')
data = pd.read_csv('results/joshimath_complete_en_ner_gender_sentiment.csv')

all = 0
all_pos = 0
all_neg = 0
all_neu = 0

male = 0
female = 0
org = 0
male_pos = 0
female_pos = 0
org_pos = 0
male_neg = 0
female_neg = 0
org_neg = 0
male_neu = 0
female_neu = 0
org_neu = 0

# dict = {}
# dict['male'] = 0
# dict['female'] = 0
# dict['no_gender'] = 0
# dict['no_ner'] = 0

# for i in range(len(data['NER'])):
#     if data['NER'][i] == 'PERSON':
#         if data['gender'][i] == 'male':
#             dict["male"] += 1
#         elif data['gender'][i] == 'female':
#             dict["female"] += 1
#         else:
#             dict['no_gender'] += 1
#     else:
#         # if data['NER'][i] == "":
#         #     dict["no_ner"] += 1
#         #     continue
#         if data['NER'][i] in dict:
#             dict[data['NER'][i]] += 1
#         else:
#             dict[data['NER'][i]] = 1

# for (k, v) in dict.items():
#     print(k, "\t", v)

for i in range(len(data['NER'])):
    all += 1
    if data['sentiment_score'][i] > 0:
        all_pos += 1
    elif data['sentiment_score'][i] < 0:
        all_neg += 1
    else:
        all_neu += 1

    if data['NER'][i] == 'PERSON':
        if data['gender'][i] == 'male':
            male += 1
            if data['sentiment_score'][i] > 0:
                male_pos += 1
            elif data['sentiment_score'][i] < 0:
                male_neg += 1
            else:
                male_neu += 1
        elif data['gender'][i] == 'female':
            female += 1
            if data['sentiment_score'][i] > 0:
                female_pos += 1
            elif data['sentiment_score'][i] < 0:
                female_neg += 1
            else:
                female_neu += 1
    else:
        org += 1
        if data['sentiment_score'][i] > 0:
            org_pos += 1
        elif data['sentiment_score'][i] < 0:
            org_neg += 1
        else:
            org_neu += 1

print("all : ", all)
print("all_pos : ", all_pos)
print("all_neg : ", all_neg)
print("all_neu : ", all_neu)

print("male : ", male)
print("male_pos : ", male_pos)
print("male_neg : ", male_neg)
print("male_neu : ", male_neu)

print("female : ", female)
print("female_pos : ", female_pos)
print("female_neg : ", female_neg)
print("female_neu : ", female_neu)

print("org : ", org)
print("org_pos : ", org_pos)
print("org_neg : ", org_neg)
print("org_neu : ", org_neu)
