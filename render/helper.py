import requests


# Odd is profane
def is_profane(s):
    url = "https://www.purgomalum.com/service/containsprofanity"

    payload = {"text": s}

    resp = requests.get(url, params=payload)

    print("Is it profane: ", resp.text)

    return resp.text == "true"