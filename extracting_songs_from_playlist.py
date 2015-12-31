#Deps: pip install soundcloud
import soundcloud
import json
client = soundcloud.Client(client_id='852f18e21a0f5fff8061415fdbb04691')

link = raw_input("enter playlist link from soundcloud ")
res = client.get('/resolve', url=link)

playlist = client.get("/playlists/"+str(res.id)+"/")

print "Title of your playlist"
print playlist.title 
print "\n"
yo =  json.dumps(playlist.tracks) 
aye = json.loads(yo)

#method of printing from json data is a bit hacky
print "Playlist content:"
for i in xrange(yo.count('bpm')):
	print (i,aye[i]["title"],aye[i]["id"])
	


	
