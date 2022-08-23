import os
import numpy as np
import pandas as pd
import tweepy
from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob    #sentiment kütüphanelerinden biri

consumer_key="?"
consumer_secret="?"
access_token="?"
acces_token_secret="?"

aoth=tweepy.Oauthhandler(consumer_key, consumer_secret, access_token, acces_token_secret)
api=tweepy.API(auth)
timeline_tweets=api.home_timeline(count=50)    
#50 yazmazsk default 20 tweet getirir 
print(timeline_tweets[0].text)
print(timeline_tweets[1].retweet_count)

# twitterda data science ile ilgili twwetleri analiz edicez
ds_tweets=api.search_tweets(q=’DataScience’ – filter:’retweet’,  tweet_mode=’extended’, count=100)
# search_tweet max 140 karakter gösteriyor bu yüzden tweer_moed=’extended’ ekliyoruz tweet 140 karakterden büyükse getirsin 100 tweet getircek. –retweetleri getirmeyecek
# sırasıyla tweetlwei okuması için iterator oluşturuyoruz
ds_list= []
for i in ds_tweets:
    Clean_tweet=re.sub(“#/https([\s]+)/@ ([\s]+)/RT ”, “”,i.full_text )
    Analiz=TextBlob(clean_tweet)
    Ds_list.append([clean_tweet, analiz.sentiment.polarity, analiz.sentiment.subjectivity])
    Df_tweets=pd.DataFrame(data=ds_list, columns=[“Tweet”, “Polarity”, “Subjectivity”])
# analiz kısmında polarity(pozitif+1 negatif -1) ve subjectivity(yorum mu nesnel bişey mi) e bakıyoruz. Data frame oluşturarak tabloya dönüştürüyoruz.

stop_w= STOPWORDS I
string_tweets=str(df_tweets[“Tweet].values)
# stopwords kelimeleri can haven’t  is gibi cümlede çok geçen ancak bir anlamı olmayan kelimelerl

word_cloud= WordCloud(stopwords=stop_w, background_color=”white”, width=1500, height=1000).generate(string_tweets)
word_cloud.to_image()
word_cloud.to_image(“word.png”)
# word görselini export eder
word_cloud.to_image().show()

#Metinde en falz  geçen kelimelerin gösterilmesi.

