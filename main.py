import comment_reader
import comment_sorting

if __name__ == "__main__":

    code = 200

    file = open("data/path.txt", "r")
    links = [N.strip() for N in file.readlines()]
    file.close()

    for link in links:
        if link.startswith("http"):
            id = link.split("=")[1].split("&")[0]
        elif len(link) == 11:
            id = link
        else:
            print("에러")
            code = 400

        print(id)

        if code == 200:
            max_comments = 500
            max_comments = int(input("어느만큼 댓글을 수집하시겠습니까? : "))

            data = comment_reader.readComment(id, max_comments)

            comment_sorting.sortComment(data)
