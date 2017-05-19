import json
import tweepy
from unidecode import unidecode
consumerKey = "OpoU1NVwjJG10CaOha2dIxRNV"
consumerSecret = "CNalebUgxtOSRslqa6jIYG1jrClN7jmdgfLRy6uLWGHgy2F5LD"
accessToken = "264393644-QNWT83AsCwmFWh3sUYtwOskanupoRh5IB4JRnC0r"
accessTokenSecret = "N2yU04KEX0b00S874Lm1iNagGwDTXUDD3dc4YqzXQ95kM"

auth1 = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth1.set_access_token(accessToken, accessTokenSecret)
api1 = tweepy.API(auth1)


trends = api1.trends_place(1)
trendsAscii = unidecode(str(trends))
dados = open("arquivo.txt","w")
dados.write(json.dumps(trendsAscii, sort_keys=True, indent=4))
dados.close()