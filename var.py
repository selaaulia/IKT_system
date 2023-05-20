import requests as rq

url = "http://152.69.160.154/api"


def getPenguji():
    data = rq.get(url + "/penguji").json()
    return [(item["name"], item["id"]) for item in data]


def getTransformator():
    data = rq.get(url + "/transformator").json()
    return [(item["name"], item["id"]) for item in data]


def savePenguji(name):
    return rq.post(url + "/penguji", json={"name": name})


def saveTransformator(name):
    return rq.post(url + "/transformator", json={"name": name})
