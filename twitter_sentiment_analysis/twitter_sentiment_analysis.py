from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sentiment_mod as s
import time
import json
##from twitterapistuff import *




#consumer key, consumer secret, access token, access secret.
ckey="lTTNClJFWAcFyVOhkRQmoxZqv"
csecret="SoYJ72SKWIqAMCiQPzE794pYZkbLuyWO2DI0bRYn8cC3OZyJqB"
atoken="1004636624267894784-2NghqL2IfU6HISn58VbXrf6xJT9wPN"
asecret="PHZWRXUFMD8JxzpXOUPNGvOBl15Ao1FPWNSz5I6NIqir1"

class listener(StreamListener):
    
    def on_data(self, data):
        try:    
            all_data = json.loads(data)

            tweet = all_data["text"]
            sentiment_value , confidence = s.sentiment(tweet)
               
            print((tweet,sentiment_value,confidence))

            if confidence*100 >=80:
                output = open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write('\n')
                output.close()
                
            return True
        except:
            return True
    def on_error(self, status):
        print (status)
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["obama"])
