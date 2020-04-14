import tkinter as tk
import requests
import json

API_KEY = 'API_KEY'
USER_AGENT = 'Ongatchi'


def lastfm_get(payload):
    headers = {'user-agent': USER_AGENT}
    url = 'http://ws.audioscrobbler.com/2.0/'

    payload['api_key'] = API_KEY
    payload['format'] = 'json'
    payload['limit'] = '1'

    response = requests.get(url, headers=headers, params=payload)
    return response

def seek_food(l):
	r = lastfm_get({
		'method': 'user.getRecentTracks',
		'user': 'jthemage'
	})

	print(r)

	l['album'] = r.json()['recenttracks']['track'][0]['album']['#text']
	l['artist'] = r.json()['recenttracks']['track'][0]['artist']['#text']
	l['song']= r.json()['recenttracks']['track'][0]['name']


latest = {}
seek_food(latest)

print(latest)

root = tk.Tk()

current_playing = "Really liking " + latest['song'] + " by " + latest['artist'] 

msg = tk.Message(root, text=current_playing)
msg.config(bg='black',fg='white', font=('times', 20))
msg.pack()

root.mainloop()