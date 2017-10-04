import time
import tweepy
import pandas as pd

auth = tweepy.OAuthHandler("3MaVOHOJEaXWB02WEnDluef8v","GEMmH6KVWR5zn68YtXGuNgBEJwC17qlX70882yYa0v8kLw9P8P")
auth.set_access_token("318156630-PxXG7R4srTywKHW3vK9DV2rlI8mw39yFcptvaUex","xVbt6LIiNT1QvL5KB3oqBQBxNk5LG77RnPFqzbGvUHOhN")

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