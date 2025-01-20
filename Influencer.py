class Influencer:
    """
    Influencer Class is responsible for managing the actions related to the influencer
    """

    def __init__(self, name):
        self.name = name
        self.followers = set()  # Track unique followers
        self.posts = []
        self.post_views = {}  # Track views for each post

    def add_post(self, post):
        self.posts.append(post)
        self.post_views[post.postId] = 0  # Initialize views for the post

    def delete_post(self,postId):
        self.posts = [post for post in self.posts if postId!=postId]
        self.post_views.pop(postId,None)

    def get_stats(self):
        return len(self.followers), {post.postId: self.post_views[post.postId] for post in self.posts}