from konlpy.tag import Okt

okt = Okt()


def labellingComments(data):
    nouns = {}

    for comment, likes, sentiment in data:
        commentNouns = okt.nouns(comment)
        for noun in commentNouns:
            if len(noun) > 1:
                if not nouns.keys().__contains__(noun):
                    nouns[noun] = {
                        "comments": [],
                        "score": likes * sentiment
                    }
                else:
                    nouns[noun]["score"] += likes * sentiment
                nouns[noun]["comments"].append((comment, likes * sentiment))
    return nouns


def sortComment(data):
    result = {}

    sorted_data = sorted(data.items(), key=lambda x: x[1]['score'], reverse=True)

    for i in sorted_data:
        result[i[0]] = i[1]

    return result
