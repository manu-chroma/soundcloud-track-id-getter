#Deps: pip install soundcloud
import soundcloud
import json
client = soundcloud.Client(client_id='YOUR_CLIENT_ID')

link = raw_input("enter playlist url from soundcloud ")
res = client.get('/resolve', url=link)

playlist = client.get("/playlists/"+str(res.id)+"/")

print "Title of your playlist"
print playlist.title
print "\n"
yo =  json.dumps(playlist.tracks)
aye = json.loads(yo)
client = soundcloud.Client(client_id=CLIENT_ID)

#Playlist id =150058341 for mann ki baat sepetember 2015
#playlist = client.get('/playlists/150058341/')

print playlist.title
yo =  json.dumps(playlist.tracks)
aye = json.loads(yo)
i = 0

#method of printing from json data is a bit hacky
print "Playlist content:"
for i in xrange(yo.count('bpm')):
	print (i,aye[i]["title"],aye[i]["id"])
