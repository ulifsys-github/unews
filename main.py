import json, requests
from flask import Flask
query = "Google"
country = "US"
URL = f"https://api.newscatcherapi.com/v2/search?q=\"{query}\"&lang=en&countries={country}"
payload={}
headers = {
  'X-API-KEY': '_WMEd-QIu7JOiJqFcz5akhJc71cd_pImYrbF_he6ZzA'
}
r = requests.get(URL, headers=headers, data=payload)
news = json.loads(r.text)

app = Flask(__name__)
code = []
@app.route('/')
def main():
    place = 0
    for title in news["articles"]:
        code.append(f'<a href="{place}">{title["title"]}</a><br>')
        place = place + 1

    return ' '.join(code)

@app.route('/<place>')
def article(place):
    code = f"""
    <title>{news["articles"][int(place)]["title"]}</title>
    <h1>{news["articles"][int(place)]["title"]}</h1>
    <h4>Author: {news["articles"][int(place)]["author"]}</h4>
    """
    return code

app.run(port=7070)