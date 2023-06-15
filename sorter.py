from konlpy.tag import Okt


def scoring_comments(data, like):
    okt = Okt()
    count = {}
    count_x_likes = {}

    for comment, likes, sentiment in data:
        nouns = okt.nouns(comment)
        if likes >= like:
            for noun in nouns:
                if len(noun) <= 1:
                    pass
                else:
                    if not count.keys().__contains__(noun):
                        count[noun] = 1 * sentiment
                    else:
                        count[noun] += 1* sentiment
                    if not count_x_likes.keys().__contains__(noun):
                        count_x_likes[noun] = likes * sentiment
                    else:
                        count_x_likes[noun] += likes * sentiment

    return count, count_x_likes


def sortComment(data, like):

    count, count_x_likes = scoring_comments(data, like)

    sort_count = sorted(count.items(), key=lambda item: item[1], reverse=True)
    sort_count_x_likes = sorted(count_x_likes.items(), key=lambda item: item[1], reverse=True)

    print(sort_count, "\n\n", sort_count_x_likes, "\n\n\n")