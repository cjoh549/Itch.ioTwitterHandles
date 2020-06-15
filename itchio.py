import json, re, os
import urllib.request
import requests, bs4

# Grab the json file and load it
itch_json = urllib.request.urlopen("https://itch.io/bundle/520/participants.json").read(500000)

itch = json.loads(itch_json)

# loop through the participants
for x in itch['participants']:

    # get the page url
    url = x['url']

    try:
        res = requests.get(url)
    except:
        continue

    page = bs4.BeautifulSoup(res.text, "html.parser")

    # find all the links that are the same format as the twitter link
    elms = page.find_all('a', rel="me")

    tmp_file = open(os.getcwd() + '/twitterhandles.txt', 'a')

    for tmatch in elms:

        # use a regex to find a twitter handle and print it out
        check_regex = re.compile("@([A-Za-z0-9_]+)")
        check_result = check_regex.match(tmatch.text)
        
        if check_result != None:
            tmp_file.write(tmatch.text + "\n")
            print(tmatch.text)

tmp_file.close()
