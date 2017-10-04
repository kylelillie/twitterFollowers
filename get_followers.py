import time
import tweepy
import pandas as pd

auth = tweepy.OAuthHandler("OauthHandler")
auth.set_access_token("YourAccessToken")

api = tweepy.API(auth)

ids1 = []
ids2 = []

for page in tweepy.Cursor(api.followers_ids, screen_name="ABMajorProjects").pages():
    ids1.extend(page)
    time.sleep(60)

df = pd.DataFrame(ids1)
df.to_csv("MP_followers.csv")
	
for page in tweepy.Cursor(api.followers_ids, screen_name="AB_EDT").pages():
    ids2.extend(page)
    time.sleep(60)

df = pd.DataFrame(ids2)
df.to_csv("EDT_followers.csv")
