from util.reader import readComment, getIDListFromFile, linkToId
from util.sorter import sortComment, labellingComments, addDataInFile, getSavedData
from util.analyzer import analyzeTendencyComment
from util.draw import drawCircleGraph

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
    print("5 : 영상 긍정도 확인")
    print("0 : 종료")
    print()
    print()
    print()
    print()
    print()

    program = input("무슨 모드를 실행 하시겠습니까? : ")

    if program == "1":
        idList = getIDListFromFile("data/path.txt")

        print("입력된 영상 리스트\n", idList)

        max_comments = int(input("어느 만큼의 댓글을 수집하시겠습니까? : "))
        like = int(input("좋아요 얼마 이상의 댓글을 수집하시겠습니까? : "))

        for videoId in idList:
            total, data = readComment(videoId, max_comments, like)
            print("가져온 댓글 입니다\n", data)

            percent, data = analyzeTendencyComment(data)
            print("긍 부정 퍼센트\n", percent)
            print("긍 부정이 발린 댓글\n", data)

            size, data = labellingComments(data)
            print("라벨링 된 댓글\n", data)

            data = sortComment(data)
            print("정렬 된 댓글\n", data)

            addDataInFile(videoId, {"total": total, "percent": percent, "nouns_size": size, "nouns": data})

            drawCircleGraph(percent)
        input("\n\n\n계속 하시 려면 아무 거나 입력해 주세요.")
    elif program == "2":
        videoId = linkToId(input("영상 링크나 id를 입력해 주세요. : "))

        print("입력된 영상 id", videoId)

        max_comments = int(input("어느 만큼의 댓글을 수집 하시겠습니까? : "))
        like = int(input("좋아요 얼마 이상의 댓글을 수집 하시겠습니까? : "))

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

        drawCircleGraph(percent)
        input("\n\n\n계속 하실려면 아무거나 입력해주세요.")
    elif program == "3":
        print("\n\n\n현재 저장된 영상 리스트")
        print(tuple(getSavedData().keys()))
        input("\n\n\n계속 하실려면 아무거나 입력해주세요.")
    elif program == "4":
        print("\n\n\n현재 저장된 영상 리스트")
        dicts = getSavedData()
        ids = tuple(dicts.keys())
        for i in range(0, len(ids)):
            print(i, ":", ids[i])

        id = int(input("조사를 할 영상 아이디를 선택해주세요 : "))

        if id in range(0, len(ids)):
            videoID = ids[id]
            nouns = dicts[videoID]["nouns"]
            print(tuple(nouns.keys()))
            noun = input("조사 할 단어를 입력해주세요. : ")
            if noun in nouns:
                for comment in nouns[noun]["comments"]:
                    print(comment["content"],comment["score"])
                print("전체 스코어", nouns[noun]["score"])
            input("\n\n\n계속 하실려면 아무거나 입력해주세요.")
        else:
            print("존재 하지 않는 아이디 입니다.")


    else:
        return 0


if __name__ == "__main__":

    while True:
        run()
