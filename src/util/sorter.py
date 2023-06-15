from konlpy.tag import Okt
import json

okt = Okt()


def getSavedData():
    file = open("src/data/data.txt", "r")
    allData = {}
    textData = file.read()
    if not textData == "":
        allData = json.loads(textData.replace("'", "\""))
    file.close()
    return allData


def addDataInFile(videoId, data):
    allData = getSavedData()

    if not allData.keys().__contains__(videoId):
        allData[videoId] = data

    file = open("src/data/data.txt", "w")
    file.write(str(allData))
    file.close()


def labellingComments(data):
    nouns = {}

    for comment, score in data:
        commentNouns = okt.nouns(comment)
        for noun in commentNouns:
            if len(noun) > 1:
                if not nouns.keys().__contains__(noun):
                    nouns[noun] = {
                        "comments": [],
                        "score": score
                    }
                else:
                    nouns[noun]["score"] += score
                nouns[noun]["comments"].append({"content": comment, "score": score})
    return nouns


def sortComment(data):
    result = {}

    sorted_data = sorted(data.items(), key=lambda x: x[1]['score'], reverse=True)

    for i in sorted_data:
        result[i[0]] = i[1]

    return result
