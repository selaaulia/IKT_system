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


def saveInputDTM(idpenguji, idtransformator, ch4, c2h2, c2h4):
    return rq.post(
        url + "/input-dtm",
        json={
            "penguji_id": idpenguji,
            "transformator_id": idtransformator,
            "CH4": ch4,
            "C2H2": c2h2,
            "C2H4": c2h4,
        },
    )


def saveInputDPM(idpenguji, idtransformator, h2, ch4, c2h2, c2h4, c2h6):
    return rq.post(
        url + "/input-dpm",
        json={
            "penguji_id": idpenguji,
            "transformator_id": idtransformator,
            "H2": h2,
            "CH4": ch4,
            "C2H2": c2h2,
            "C2H4": c2h4,
            "C2H6": c2h6,
        },
    )

def saveResultDTM(idinputdtm, fault):
    return rq.post(
        url + "/result-dtm",
        json={
            "dtm_input_id": idinputdtm,
            "fault": fault,
        },
    )