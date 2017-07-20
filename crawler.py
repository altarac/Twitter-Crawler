import tweepy
from textblob import TextBlob

consumer_key = 'DSWRoHKbk0BDLO5VbvD3dmAVU'
consumer_secret = 'yK6DyBij7D8L6Gr1cje0jIjLSZzJoB2UBoYI6AFIXdsb6LrU53'
access_token = '554786429-fHVEYuT2kuHGeuxeK4MhnLCo7jExyrsAVsbvMlL1'
access_token_secret = 'PyzFrYpxmsbgu0Jb3fhgozN3A73KY58N4G078IsIyhRxu'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        try:
            analysis = TextBlob(status.text)
            print(status.text)
            print(analysis.sentiment)
            datafile = open('/Users/samuelaltarac/Desktop/python programs/data.txt','a')
            datafile.write(status.text)
            datafile.write('\n')
            datafile.write(str(analysis.sentiment))
            datafile.write('\n')
            datafile.close()
            
        except UnicodeEncodeError:
            print('ERROR unicode')

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['aapl', 'apple', 'tim cook', 'iphone stock', 'apple stock'])










"""
public_tweets = api.search('learn')

for tweet in public_tweets:
    try:
        print(tweet.text)
    except UnicodeEncodeError:
        print('UCS-2 codec cant encode characters in position 113-113: Non-BMP character not supported in Tk')
"""





"""
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
"""

