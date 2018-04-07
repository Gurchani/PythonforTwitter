CONSUMER_KEY = '3jlzFiMtjZgNP6mwpbjMtj8U2'
CONSUMER_SECRET = '5TNiXf8e4CAtorYWMw5oRi76JYCbn1HVvT3o90NHlQdrVMsc9M'
ACCESS_KEY = '275605019-eFkeyHZbRx2iGxV3DBoudOgH3uzpaeWep3bvBCSF'
ACCESS_SECRET = 'eTjrgHLAsc5mXajRmfngajJojih8R2KXeBSOe3Jh5JCM0'

import time
from tweepy import OAuthHandler
import tweepy
import random
import xlwt
import ssl
import pyping
import MySQLdb
import oauth2 as oauth
import json
from xlrd import open_workbook

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

subject = "mlp_officiel"
##api = tweepy.API(auth)
##
##book = open_workbook(subject + "Tweets" + '.xls')
##sheet = book.sheet_by_index(1)

##rows = sheet.max_row

#for i in enumerate(rows/100):
batch = [186835895285059586, 188353601809285121]
    

#This will get tweets of a user
Tweets = "https://api.twitter.com/1.1/statuses/lookup.json?id=" + batch
response2, data2 = client.request(recentTweets)

tweets = json.loads(data2)
print len(tweets)
for i in tweets:    
    print i["text"]
    print i["id"]





def saveDetails(userDetails):
##        fw.write(str(userDetails) + "\n" )
##        print "Saved"
        InsertQuery = ("INSERT INTO jlmelenchon "
               "(`id`, `screen_name`, `location`, `description`, `protected`, `verified`, `followers_count`, `friends_count`, `listed_count`, `favourites_count`, `statuses_count`, `created_at`, `time_zone`, `geo_enabled`, `lang`) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        for i in userDetails:                
                values = (str(i.id), i.screen_name.encode('ascii', 'ignore').decode('ascii'), i.location.encode('ascii', 'ignore').decode('ascii'), i.description.encode('ascii', 'ignore').decode('ascii'), str(i.protected), str(i.verified), i.followers_count, i.friends_count, i.listed_count, i.favourites_count, i.statuses_count, i.created_at, i.time_zone, i.geo_enabled, i.lang)
                cur.execute(InsertQuery, values)
        print "Saved"
