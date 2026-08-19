import requests

r = requests.get('https://api.github.com/events')

with open("zaid.txt", "w") as f:
    f.write(r.text)
