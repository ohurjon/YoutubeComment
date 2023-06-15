from util.reader import readComment, getIDListFromFile, linkToId
from util.sorter import sortComment, labellingComments, addDataInFile, getSavedData
from util.analyzer import analyzeTendencyComment
import os


def run():
    print("\r\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("유튜브 댓글 분석 프로그램에 오신걸 환영합니다")
    print()
    print()
    print()
    print()
    print()
    print("1 : path.txt 기반 영상 분석기 실행")
    print("2 : input 기반 영상 분석기 실행")
    print("3 : 분석된 영상 리스트")
    print("4 : 영상 단어 분석")
    print("0 : 종료")
    print()
    print()
    print()
    print()
    print()

    program = input("무슨 모드를 실행 하시겠습니까? : ")

    if program == "1":
        idList = getIDListFromFile("src/data/path.txt")

        print("입력된 영상 리스트\n", idList)

        max_comments = int(input("어느 만큼의 댓글을 수집하시겠습니까? : "))
        like = int(input("좋아요 얼마 이상의 댓글을 수집하시겠습니까? : "))

        for videoId in idList:
            data = readComment(videoId, max_comments, like)
            print("가져온 댓글 입니다\n", data)

            percent, data = analyzeTendencyComment(data)
            print("긍 부정 퍼센트\n", percent)
            print("긍 부정이 발린 댓글\n", data)

            data = labellingComments(data)
            print("라벨링 된 댓글\n", data)

            data = sortComment(data)
            print("정렬 된 댓글\n", data)

            addDataInFile(videoId, {"percent": percent, "nouns": data})
        input("\n\n\n계속 하실려면 아무거나 입력해주세요.")
    elif program == "2":
        videoId = linkToId(input("영상 링크나 id를 입력 해주세요. : "))

        print("입력된 영상 id", videoId)

        max_comments = int(input("어느 만큼의 댓글을 수집하시겠습니까? : "))
        like = int(input("좋아요 얼마 이상의 댓글을 수집하시겠습니까? : "))

        data = readComment(videoId, max_comments, like)
        print("가져온 댓글 입니다\n", data)

        percent, data = analyzeTendencyComment(data)
        print("긍 부정 퍼센트\n", percent)
        print("긍 부정이 발린 댓글\n", data)

        data = labellingComments(data)
        print("라벨링 된 댓글\n", data)

        data = sortComment(data)
        print("정렬 된 댓글\n", data)

        addDataInFile(videoId, {"percent": percent, "nouns": data})
        input("\n\n\n계속 하실려면 아무거나 입력해주세요.")
    elif program == "3":
        print("\n\n\n현재 저장된 영상 리스트")
        print(tuple(getSavedData().keys()))
        input("\n\n\n계속 하실려면 아무거나 입력해주세요.")
    elif program == "4":
        pass
    else:
        return 0
