#This tweet gives you a list of most active retweeters of a perticular user and puts them in an excel sheet and also in mysql databse
#Change "Subject"to get details on the twitter user of your own choice

import oauth2 as oauth
import json
import xlrd
import xlwt
from xlutils.copy import copy
import time
import pyping
import MySQLdb

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

db = MySQLdb.connect(host="",    # your host, usually localhost
                     user="",         # your username
                     passwd="",  # your password
                     db="",
                     use_unicode=True,
                     charset="utf8")        # name of the data base

cur = db.cursor()

Subject = "Marion_M_Le_Pen"
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
    











    
    
