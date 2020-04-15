import tkinter as tk
import requests
import json

# Get API key
f = open("credentials.txt","r+")
API_KEY = f.readline()
f.close()

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
	l.clear()

	r = lastfm_get({
		'method': 'user.getRecentTracks',
		'user': 'jthemage'
	})

	print(r)

	l['album'] = r.json()['recenttracks']['track'][0]['album']['#text']
	l['artist'] = r.json()['recenttracks']['track'][0]['artist']['#text']
	l['song']= r.json()['recenttracks']['track'][0]['name']
	print(l)


latest = {}

class Ongatchi(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		self.faces = {
			'sleep':	'( ︶ ︿︶ )',
			'happy':	'( ◕ ‿ ◕ )',
			'sad0':		'( ⚆ _ ⚆ )',
			'sad1': 	'( ಠ _ ಠ )',
			'sad2':		'( ¬ _ ¬ )',
			'dead':		'( X _ X )'
		}

		self.face = tk.StringVar(root)
		self.face.set(self.faces['sleep'])

		self.og = tk.Message(root, textvariable=self.face)
		self.og.config(font=('times', 30), width=450)
		self.og.pack()

		self.display_text = tk.StringVar(root)
		self.display_text.set("ZZZZZZ...")

		self.msg = tk.Message(root, textvariable=self.display_text)
		self.msg.config(font=('times', 15), width=450)
		self.msg.pack()

		# Debug button
		self.b = tk.Button(root, text="give food pls", command=self.eat)
		self.b.pack()

		self.previous = {}

	def eat(self):
		seek_food(latest)

		if latest != self.previous:
			self.display_text.set("Really liking " + latest['song'] + " by " + latest['artist'] + "!")
			self.previous = latest
		else:
			self.display_text.set("Listen to something new...")

if __name__ == "__main__":
	root = tk.Tk()
	root.title("ongatchi Alpha 1.0")
	root.geometry('450x450')
	on = Ongatchi(root)
	on.pack(side="top", fill="both", expand=True)
	root.mainloop()