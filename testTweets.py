import oauth2 as oauth
import json
import MySQLdb

#Database
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="tweets",
                     use_unicode=True,
                     charset="utf8")        # name of the data base

cur = db.cursor()

CONSUMER_KEY = '3jlzFiMtjZgNP6mwpbjMtj8U2'
CONSUMER_SECRET = '5TNiXf8e4CAtorYWMw5oRi76JYCbn1HVvT3o90NHlQdrVMsc9M'
ACCESS_KEY = '275605019-eFkeyHZbRx2iGxV3DBoudOgH3uzpaeWep3bvBCSF'
ACCESS_SECRET = 'eTjrgHLAsc5mXajRmfngajJojih8R2KXeBSOe3Jh5JCM0'

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

def saveDetails(userDetails):
##        fw.write(str(userDetails) + "\n" )
##        print "Saved"
        InsertQuery = ("INSERT INTO mlp_officiel_tweets"
            "(`created_at`, `id`, `text`, `source`, `truncated`, `in_reply_to_status_id`, `in_reply_to_user_id`, `in_reply_to_screen_name`, `geo`, `coordinates`, `place`, `contributors`, `retweet_count`, `favorite_count`, `lang`, `retweeted`, `favorited`)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")                       
        values = (str(i["created_at"]),str(i["id"]), i["text"].encode('ascii', 'ignore').decode('ascii'), i["source"], i["truncated"],
                  str(i["in_reply_to_status_id"]), str(i["in_reply_to_user_id"]), i["in_reply_to_screen_name"],
                  i["geo"], str(i["coordinates"]), str(i["place"]), str(i["contributors"]), str(i["retweet_count"]), i["favorite_count"], i["lang"],
                                                      i["retweeted"], i["favorited"])
        cur.execute(InsertQuery, values)
        print "Saved"


#This will get 3200 most recent tweets of a user
recentTweets = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=mlp_officiel&count=200"
response2, data2 = client.request(recentTweets)

tweets = json.loads(data2)
print len(tweets)
for i in tweets:
    saveDetails(i)
    print i["text"]
    print i["id"]
    print i["created_at"]




