import csv
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
pd.options.mode.chained_assignment = None  # default='warn'

# data = pd.read_csv('.\outputs\joshimath_word_en_ner_test_gender.csv')
data = pd.read_csv('results/joshimath_complete_en_ner_gender.csv')

sid = SentimentIntensityAnalyzer()

data['scores'] = data['Embedded_text'].apply(lambda Embedded_text: sid.polarity_scores(Embedded_text))

data['sentiment_score']  = data['scores'].apply(lambda score_dict: score_dict['compound'])

data['overall_sentiment'] = data['sentiment_score'].apply(lambda c: 'pos' if c>0 else('neg' if c<0 else 'neutral'))


# data.to_csv('.\outputs\joshimath_word_en_ner_test_gender_scores.csv')
data.to_csv('results/joshimath_complete_en_ner_gender_sentiment.csv')












# # Get the main information of a given list of users
# # These users belongs to my following. 

# users = ['nagouzil', '@yassineaitjeddi', 'TahaAlamIdrissi',
#          '@Nabila_Gl', 'geceeekusuu', '@pabu232', '@av_ahmet', '@x_born_to_die_x']

# # this function return a list that contains : 
# # ["nb of following","nb of followers", "join date", "birthdate", "location", "website", "description"]

# users_info = get_user_information(users, headless=True)

# # Get followers and following of a given list of users Enter your username and password in .env file. I recommande
# # you dont use your main account. Increase wait argument to avoid banning your account and maximise the crawling
# # process if the internet is slow. I used 1 and it's safe.

# # set your .env file with SCWEET_EMAIL, SCWEET_USERNAME and SCWEET_PASSWORD variables and provide its path
# env_path = ".env"

# following = get_users_following(users=users, env=env_path, verbose=0, headless=True, wait=2, limit=50, file_path=None)

# followers = get_users_followers(users=users, env=env_path, verbose=0, headless=True, wait=1, limit=50, file_path=None)
