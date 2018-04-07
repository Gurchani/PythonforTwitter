import oauth2 as oauth
import json
import xlrd
import xlwt
from xlutils.copy import copy
import time
import pyping
import MySQLdb

CONSUMER_KEY = 'Q7vnH9Omri4kvXE4fkopKI9tZ'
CONSUMER_SECRET = '2ulhp2QGkw1jfA7vxfIzkZboI52G56mVXfTql21uHRwXT8Oe7l'
ACCESS_KEY = '729312774241832960-IzqShs7gPoPevNdy31KYt1axlkPUB7S'
ACCESS_SECRET = '72tf78cUaASbXEvKT3zP4aUlmjSm5dV0qwNZVicTA8X7I'

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="retweeters",
                     use_unicode=True,
                     charset="utf8")        # name of the data base

cur = db.cursor()

Subject = "lepenjm"
data = xlrd.open_workbook(Subject + "Tweets.xls")
table = data.sheet_by_name("A Test Sheet")
wb = copy(data)
s = wb.get_sheet(0)

def internet_on():       

        r = pyping.ping('4.2.2.2')
        if r.ret_code == 0:
            print("Still Holding")
            return True
        else:
            print("Down goes Frazier")
            return False

def saveDetails(tweetid, retweeterid):
##        fw.write(str(userDetails) + "\n" )
##        print "Saved"
        InsertQuery = ("INSERT INTO "+ Subject + "_retweeters "
               "(`tweetid`, `retweeterid`) "
               "VALUES (%s, %s)")               
        values = (str(tweetid), str(retweeterid))
        cur.execute(InsertQuery, values)
        print "Saved"
    

verticalCounter = 0;
for i in table.col_values(0):
    HorzontalCounter = 1
    time.sleep(12)
    retry = True  
    while retry:
            if internet_on()== True:
                print ("Connected")
                retweets = "https://api.twitter.com/1.1/statuses/retweeters/ids.json?id=" + str(i) + "&count=200&cursor=-1"    
                response, data = client.request(retweets)
                print data
                retweeters = json.loads(data)
                for j in retweeters["ids"]:
                    saveDetails(i,j)    
                retry == False
                break
            else :
                 print ("Connection Problems")
                 time.sleep(90)        
                 #code to check internet ends here
    verticalCounter = verticalCounter + 1
    



###This will get 3200 most recent tweets of a user
##recentTweets = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=mlp_officiel&count=3200"
##response2, data2 = client.request(recentTweets)
##
##tweets = json.loads(data2)
##print len(tweets)
##for i in tweets:    
##    print i["text"]
##    print i["id"]







    
    
