#Deps: pip install soundcloud
import soundcloud
import json
client = soundcloud.Client(client_id="YOUR_CLIENT_ID")
//Playlist id =150058341 for mann ki baat sepetember 2015
playlist = client.get('/playlists/150058341/')

print playlist.title
yo =  json.dumps(playlist.tracks) 
aye = json.loads(yo)
i = 0 

#method of printing from json data is a bit hacky
for i in xrange(yo.count('bpm')):
	print (i,aye[i]["title"],aye[i]["id"])
	
