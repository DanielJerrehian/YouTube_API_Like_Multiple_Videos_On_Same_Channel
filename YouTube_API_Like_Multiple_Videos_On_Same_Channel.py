from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from apikey import apikey
# step 1 : API key
# step 2 : outh 2.0 name it  client_secret.json
# step 3 : set client secret equal to 'CLIENT_SECRET_FILE' variable
# step 3 : channelId to desired YouTube Channel ID of videos 
# step 4 : the number of videos to be liked, acceptable values are 1 to 50, inclusive


class YoutubeLike:
    CLIENT_SECRET_FILE = 'CLIENT SECRET' # step 1 : set client secret
    SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_console()
    youtube = build('youtube', 'v3', credentials=credentials)

    def getVids(self):
        ids = [] # store video IDs
        youtube = build('youtube', 'v3', developerKey=apikey)
        channelId = "CHANNEL ID" # step 3 : channelId to your youtube channels id
        maxResults = 50 # step 4 : 'maxResults' the number of videos to be liked, acceptable values are 1 to 50, inclusive
        request = youtube.search().list(part="snippet",channelId=channelId,maxResults=maxResults,order="videoCount",type="video")
        response = request.execute()
        for item in response['items']:
            print(item['snippet']['title'])
            ids.append((item['id']['videoId'], item['snippet']['channelId']))
        print(response)
        return ids
    def likeVids(self):
        ids = self.getVids()
        for videoId in ids:
            self.youtube.videos().rate(rating='like', id=videoId[0]).execute()
	
        
like_videos = YoutubeLike()
like_videos.likeVids()
