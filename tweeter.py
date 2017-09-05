#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from emojilist import emojis
emoji_set = set(emojis)
from pprint import pprint
import json

#Variables that contains the user credentials to access Twitter API
access_token = "732697352-ahcdVGJ6bIdKqrQPjKsXh56VSGNGMbSnQ57odpRh"
access_token_secret = "w8kbzyWnAmgPYjGJie7tVPKWKxINYN17p3b6puTVelaz1"
consumer_key = "YeMgArjEGGYUwR9tJJm0tFi8x"
consumer_secret = "s7twuA5ahV9dO5uij6UPB3flE2TWlh2oDBk2cuBw5Ifg2bihO0"

# def clear_rt(t):
#     return t[t.find(':')+2:] if t.startswith('RT') else t

def tokenize(t):
    return t.strip().split(' ')

def is_not_link(w):
    return not w.startswith('https://') and not w.startswith('http://')

def is_not_someone(w):
    return not w.startswith('@')

def is_legit_word(w):
    return is_not_link(w) and is_not_someone(w)

def remove_hashtag(w):
    return w[1:] if w.startswith('#') else w

def clean_t(t):
    tokens = tokenize(t.replace('\n', ' '))
    return ' '.join(map(remove_hashtag, filter(is_legit_word, tokens)))


def is_data_keep(res):
    # use only un-truncated English text responses
    return 'text' in res and not res['truncated'] and res['lang']=='en'

def got_some_emoji(t):
    # return True iff:
    # given t ends with emoji and has two or more emojis in it.
    return t[-1] in emoji_set and sum(1 if char in emoji_set else 0 for char in t) >= 3

def is_text_keep(t):
    # decided to keep the text if it is not a retweet and ends with an emoji
    return t and not t.startswith('RT') and got_some_emoji(t)



#This is a basic listener that just prints received tweets to stdout.
class MyListener(StreamListener):

    def __init__(self, file):
        super()
        self.outfile = file

    def on_data(self, res):
        res = json.loads(res)
        if is_data_keep(res):
            t = clean_t(res['text'])
            if is_text_keep(t):
                #pprint(res)#; raise 'something'
                t = clean_t(res['text'])
                print(t)
                self.outfile.write(t+'\n')
        return True

    def on_status(self, status):
        print(status.text)

    def on_error(self, status):
        print('status code: {}'.format(status))

def main():
    l = MyListener(open('north.txt','w'))
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=list(('north')))#,async=True)
    #stream.filter(track=list(emoji_set))

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    main()
