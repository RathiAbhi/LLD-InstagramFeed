class Hashtag:
    """
    class to manage a hastag
    """
    def __init__(self,name):
        self.name = name
        self.posts = []
        self.followers = set()

    def addPost(self,post):
        self.posts.append(post)