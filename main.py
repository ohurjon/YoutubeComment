
# import googleapiclient.discovery
# from konlpy.tag import Kkma
#
# import data
# import key
#
# kkma = Kkma()
#
#
# # 대충 수정된 부분
# def getData(videoID="", pageToken=""):
#     api_service_name = "youtube"
#     api_version = "v3"
#     DEVELOPER_KEY = key.YOUTUBE_API_KEY
#
#     youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)
#
#     request = youtube.commentThreads().list(
#         pageToken=pageToken,
#         part="snippet",
#         maxResults=100,
#         textFormat="plainText",
#         videoId=videoID
#     )
#     response = request.execute()
#
#     return response
#
#
# if __name__ == "__main__":
#
#     code = 200
#
#     link = input("유튜브 링크나 영상 id를 입력해주세요. : ")
#
#     if link.startswith("http"):
#         id = link.split("=")[1]
#     elif len(link) == 11:
#         id = link
#     else:
#         code = 400
#         raise ValueError
#
#     if code == 200:
#         print("입력된 영상 id : " + id)
#         nouns = {}
#
#         for i in getData(videoID=id)["items"]:
#             comment = i["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
#             # print(comment)
#
#             for noun in kkma.nouns(comment):
#                 # print(noun,end="_")
#                 if len(noun) >= 2:
#                     if not nouns.keys().__contains__(noun):
#                         nouns[noun] = 1
#                     else:
#                         nouns[noun] += 1
#
#         for i in list(nouns.keys()):
#             if i in data.abuse:
#                 del nouns[i]
#
#         print(sorted(nouns.items(), key=lambda item: item[1], reverse=True))
import googleapiclient.discovery
from konlpy.tag import Kkma

import data
import key

kkma = Kkma()


# 대충 수정된 부분
def getData(videoID="", pageToken=""):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = key.YOUTUBE_API_KEY

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        pageToken=pageToken,
        part="snippet",
        maxResults=100,
        textFormat="plainText",
        videoId=videoID
    )
    response = request.execute()

    return response


if __name__ == "__main__":
    code = 200

    link = input("유튜브 링크나 영상 id를 입력해주세요. : ")

    if link.startswith("http"):
        id = link.split("=")[1]
    elif len(link) == 11:
        id = link
    else:
        code = 400
        raise ValueError

    if code == 200:
        print("입력된 영상 id : " + id)
        nouns = {}
        user_words = input("여러 번 입력한 단어들을 공백으로 구분하여 입력하세요: ").split()

        for i in getData(videoID=id)["items"]:
            comment = i["snippet"]["topLevelComment"]["snippet"]["textOriginal"]

            for noun in kkma.nouns(comment):
                if len(noun) >= 2:
                    if noun in user_words:
                        if noun not in nouns:
                            nouns[noun] = 1
                        else:
                            nouns[noun] += 1

        for i in list(nouns.keys()):
            if i in data.abuse:
                del nouns[i]

        print(sorted(nouns.items(), key=lambda item: item[1], reverse=True))
#자신이 원하는 단어들을 입력하면 댓글에서 그에 대한 단어의 빈도수를 빈도수가 많은 숫자대로 출력하는 프로그램

