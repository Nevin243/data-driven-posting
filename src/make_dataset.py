import requests

URL = "https://dev.to/api/articles"
payload = {"page":1}
page = 1
REQS = 3001
STEP = 1

f = open("./../../data/raw/raw.txt", "w+")

try:
    while payload["page"] < REQS:
        
        r = requests.get(URL, params=payload)
        r.raise_for_status()
        
        f.write(r.text)
        payload["page"]+=STEP
    
except:
    print("Something broke...")

finally:
    f.close()


