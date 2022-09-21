import requests

r = requests.get('https://animechan.vercel.app/api/random') #Get animechan API
f = r.json() #Get json data
print(f"Anime: {f['anime']}\nChara: {f['character']}\nQuote: {f['quote']}") #Print Json data
