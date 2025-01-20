class Post:
    post_counter = 1
    """
    a class to handle the management of the post and its structure
    """
    def __init__(self,influencer,message,hashtags,timestamp):
        self.postId = Post.post_counter
        Post.post_counter += 1
        self.influencer = influencer
        self.message = message
        self.hashtags = hashtags
        self.timestamp = timestamp