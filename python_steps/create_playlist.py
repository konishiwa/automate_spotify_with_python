# Step 1: Map out all the steps used to create a playlist 
import json
from secrets import spotify_user_id, spotify_token

class CreatePlaylist: 
    
    # constructor
    def __init__(self): 
        pass

    # 1. Log into Youtube
    def get_youtube_client(self):
        pass 

    # 2. Grab Liked Videos
    def get_liked_videos(self):
        pass

    # 3a. Create A New Playlist 
    def create_new_playlist(self):
        request_body = json.dumps({
            "name": "youtube bops",
            "descr": "Videos liked on youtube, automatically imported through python",
            "public": True
        })
        #endpoint for create a playlist 
        query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id)
        response = requests.post(
            query, 
            data = request_body,
            headers{
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response_json["id"]
        
        #returns playlist id, will need later to edit playlist
        return response_json["id"]


    # 3b. Add spotify URI 
    def get_spotify_uri(self):
        pass

    # 4. Add Song to New Spotify Playlist 
    def add_new_song(self):
        pass