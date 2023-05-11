import pandas as pd
# from nltk import FreqDist
import nltk, collections, re
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

df = pd.read_csv('results/joshimath_complete_en.csv')

def preprocessing(text):
    # removing punctuations, unwanted characters and converting to lowercase
    text = re.sub("[^-9A-Za-z ]", "", text).lower()
    # removing stopwords and tokenizing
    stop = stopwords.words("english")
    tokens = [word for word in (token for token in word_tokenize(text)) if word not in stop]

    i = 0
    while i < len(tokens):
        if tokens[i] == "savejoshimath":
            tokens[i] = "save"
            if i+1 < len(tokens):
                tokens[i+1] = "joshimath"
            else:
                tokens.append("joshimath")
        elif tokens[i] == "joshimathcrisis":
            tokens[i] = "joshimath"
            if i+1 < len(tokens):
                tokens[i+1] = "crisis"
            else:
                tokens.append("crisis")
        elif tokens[i] == "joshimathsinking":
            tokens[i] = "joshimath"
            if i+1 < len(tokens):
                tokens[i+1] = "sinking"
            else:
                tokens.append("sinking")
            tokens[i+1] = "sinking"
        elif tokens[i] == "joshimathissinking":
            tokens[i] = "joshimath"
            if i+1 < len(tokens):
                tokens[i+1] = "is"
            else:
                tokens.append("is")

            if i+2 < len(tokens):
                tokens[i+1] = "sinking"
            else:
                tokens.append("sinking")            
        i += 1

    # lemmatizing
    lmtzr = nltk.WordNetLemmatizer()
    preprocessed_text = ' '.join([lmtzr.lemmatize(word) for word in tokens])
    return preprocessed_text

def show_ngrams(tokenized, n):
    esNgrams = ngrams(tokenized, n)
    # get the frequency of each ngram in our corpus
    esNgramsFreq = collections.Counter(esNgrams)
    if n==1 :
        ls =  esNgramsFreq.most_common(21)
        for i in ls:
            # print(i[0], ", ")
            print(i)
    else:
        ls =  esNgramsFreq.most_common(11)
        for i in ls:
            print(i)
            # print(i[0], ", ")

text = ""
for i in range(len(df['Embedded_text'])):
    text += ". "
    text += df['Embedded_text'][i]

text = preprocessing(text)

file = open("results/all_tweets.txt","w+")
file.write(str(text))
file.close()

tokenized = text.split()
# print(str(tokenized))

print("\n 20 top unigrams are:")
show_ngrams(tokenized, 1)

print("\n 10 top bigrams are:")
show_ngrams(tokenized, 2)

# print("\n 50 top trigrams are:")
# show_ngrams(tokenized, 3)




















# unigrams = []

# def get_unigrams(text):
#     # print(text)
#     tokens = text.split()
#     for a in tokens:
#         unigrams.append(a)    
#         # print(a)

#     # ls = ngrams(tokens, 1)
#     # unigrams.extend(ls)    
#     # unigramsfreq = collections.Counter(ls)
#     # unigramsfreq.most_common(50)


# for i in range(len(df['Embedded_text'])):
#     get_unigrams(df['Embedded_text'][i])


# unigramsfreq = Counter(unigrams)
# unigramsfreq.most_common(50)

# # unigrams_freq = {}
# # for a in unigrams:
# #     if a in unigrams_freq:
# #         unigrams_freq[a] += 1
# #     else:
# #         unigrams_freq[a] = 1

# # for k, v in unigrams_freq.items():
# #     print(k, " ", v)
    