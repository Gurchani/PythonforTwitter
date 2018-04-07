import time
from tweepy import OAuthHandler
import tweepy
import random
import xlwt
import ssl
import pyping
import MySQLdb

#Database
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="retweeters",
                     use_unicode=True,
                     charset="utf8")        # name of the data base

cur = db.cursor()

subject = "mlp_officiel"

ckey = '3jlzFiMtjZgNP6mwpbjMtj8U2'
csecret = '5TNiXf8e4CAtorYWMw5oRi76JYCbn1HVvT3o90NHlQdrVMsc9M'
atoken = '275605019-eFkeyHZbRx2iGxV3DBoudOgH3uzpaeWep3bvBCSF'
asecret = 'eTjrgHLAsc5mXajRmfngajJojih8R2KXeBSOe3Jh5JCM0'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

def getretweeterList():
    Query = ("SELECT retweeterid, COUNT(*) AS magnitude" 
            " FROM " + subject +"_retweeters "
            " GROUP BY retweeterid "
            " ORDER BY magnitude DESC " 
            " LIMIT 500")
    cur.execute(Query)
    return cur
        

def internet_on():       

        r = pyping.ping('4.2.2.2')
        if r.ret_code == 0:
            print("Still Holding")
            return True
        else:
            print("Down goes Frazier")
            return False

def lookup_user_list(followers_id, api):    
    full_users = []
    users_count = len(followers_id)
    while True:
         try:
             for i in range((users_count / 100) + 1):
                 full_users.extend(api.lookup_users(user_ids=followers_id[i*100:min((i+1)*100, users_count)]))
                 print  ('getting users batch:' + str(i))
                 #Code to Make sure Internet is Connected
                 retry = True    
                 while retry:
                    if internet_on()== True:
                        print ("Connected")
                        retry == False
                        break
                    else :
                        print ("Connection Problems")
                        time.sleep(90)
                 #code to check internet ends here
         except tweepy.TweepError as e:
             print ('Something went wrong, quitting...', e)             
         return full_users

def saveDetails(userDetails, retweetedNumber):
##        fw.write(str(userDetails) + "\n" )
##        print "Saved"
        counter = 0
        InsertQuery = ("INSERT INTO " + subject + "_retweeters_profile "
               "(`id`, `screen_name`, `Retweeted`, `location`, `description`, `protected`, `verified`, `followers_count`, `friends_count`, `listed_count`, `favourites_count`, `statuses_count`, `created_at`, `time_zone`, `geo_enabled`, `lang`) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        for i in userDetails:                
                values = (str(i.id), i.screen_name.encode('ascii', 'ignore').decode('ascii'), str(retweetedNumber[counter]),  i.location.encode('ascii', 'ignore').decode('ascii'), i.description.encode('ascii', 'ignore').decode('ascii'), str(i.protected), str(i.verified), i.followers_count, i.friends_count, i.listed_count, i.favourites_count, i.statuses_count, i.created_at, i.time_zone, i.geo_enabled, i.lang)
                cur.execute(InsertQuery, values)
                counter = counter + 1
        print "Saved"
listofTopretweeters = []
timesRetweeted = []
for i in getretweeterList():
    listofTopretweeters.append(i[0])
    timesRetweeted.append(i[1])
    

userObjects = lookup_user_list(listofTopretweeters, api)
saveDetails(userObjects, timesRetweeted)
    
    
        
