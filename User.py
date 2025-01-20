class User:
    def __init__(self, name):
        self.name = name
        self.followed_entities = set()  # Can hold influencers and hashtags
        self.feed = []

    def follow(self, entity):
        self.followed_entities.add(entity)

    def fetch_feed(self):
        return self.feed