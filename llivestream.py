import tweepy
SEP = ';'
csv = open('OutputStreaming.csv','w',encoding='utf-8')
csv.write('Date' + SEP + 'Text' + SEP + 'Location' + SEP + 'Number_Follower' + SEP + 'User_Name' + SEP + 'Friends_count\n')

class MyStreamListener(tweepy.Stream):

    def __init__(self, *args):
        super().__init__(*args)

    def send_data(*args):
        twtr_stream = MyStreamListener(*args)

        twtr_stream.filter(track=['tweepy'])
    def on_status(self, status):
        Created = status.created_at.strftime("%Y-%m-%d-%H:%M:%S")
        Text = status.text.replace('\n', ' ').replace('\r', '').replace(SEP, ' ')
        Location = ''
        if status.coordinates is not None:
            lon = status.coordinates['coordinates'][0]
            lat = status.coordinates['coordinates'][1]
            Location = str(lat) + ',' + str(lon)
        Follower = str(status.user.followers_count)
        Name = status.user.screen_name
        Friend = str(status.user.friends_count)
        csv.write(Created + SEP + Text + SEP + Location + SEP + Follower + SEP + Name + SEP + Friend + '\n')
    def on_error(self, status_code):
        print(status_code)

consumer_key = '19xq7DLv7lLRhsmvQ2Q2CMnqF'
consumer_secret = 'gh5pjvQzNCuLwWZYbStCJtFPZq8rmXQLdk6qgqv1tZDw6ZEM5p'
access_token = '763736486390829058-pwAY3iyYrUJZFxuZm0LwiRx8v0ngrst'
access_token_secret = 'w8Z0JMLjvmymHOhePibU5whddikYWbzhmEWgvXY5sfOGm'

# stream
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
myStream = MyStreamListener(consumer_key,consumer_secret,access_token, access_token_secret)
myStream.filter(track=['#'])
