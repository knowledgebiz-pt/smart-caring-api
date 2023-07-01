import core.models as model


def merge_news_user(news: model.news_model.News(), users: model.user_model.User()):
    """
    Merge news and user models
    :param news:
    :param users:
    :return:
    """
    for news_article in news:
        print(type(news_article))
        for user in users:
            if news_article["user_id"] == user["_id"]["$oid"]:
                news_article["user"] = {
                    "name": user["name"],
                    "email": user["email"],
                    "user_gender": user["user_gender"],
                    "user_type": user["user_type"],
                    "visibility": user["visibility"],
                    "picture": user["picture"],
                }
    return news
