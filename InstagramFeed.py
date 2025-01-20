from Hashtag import Hashtag
from Influencer import Influencer
from Post import Post
from User import User


class InstagramFeed:
    def __init__(self):
        self.influencers = {}
        self.users = {}
        self.hashtags = {}

    def create_entity(self, entity_type, name):
        if entity_type == "Influencer":
            self.influencers[name] = Influencer(name)
            print(f"Created Influencer: {name}")
        elif entity_type == "User":
            self.users[name] = User(name)
            print(f"Created User: {name}")

    def follow(self, entity_name, user_name):
        user = self.users.get(user_name)
        if not user:
            print(f"User {user_name} does not exist.")
            return

        if entity_name.startswith("#"):
            hashtag = self.hashtags.get(entity_name[1:])
            if not hashtag:
                hashtag = Hashtag(entity_name[1:])
                self.hashtags[entity_name[1:]] = hashtag

            user.follow(hashtag)
            hashtag.followers.add(user)
            print(f"User {user_name} followed hashtag {entity_name}.")
        else:
            influencer = self.influencers.get(entity_name)
            if not influencer:
                print(f"Influencer {entity_name} does not exist.")
                return
            user.follow(influencer)
            influencer.followers.add(user)
            print(f"User {user_name} followed influencer {entity_name}.")

    def post(self, influencer_name, message, hashtags):
        influencer = self.influencers.get(influencer_name)
        if not influencer:
            print(f"Influencer {influencer_name} does not exist.")
            return

        hashtags_objs = []
        for hashtag_name in hashtags:
            hashtag = self.hashtags.setdefault(hashtag_name, Hashtag(hashtag_name))
            hashtags_objs.append(hashtag)

        # Create the post and let the Post class handle the post ID
        post = Post(influencer, message, hashtags_objs, timestamp=len(influencer.posts))
        influencer.add_post(post)

        for hashtag in hashtags_objs:
            hashtag.addPost(post)
        for follower in influencer.followers:
            follower.feed.append(post)

        print(f"Post created by {influencer_name}: {message}")

    def fetch(self, user_name):
        user = self.users.get(user_name)
        if not user:
            print(f"User {user_name} does not exist.")
            return []

        # Collect posts from influencers the user follows
        user_feed = set(user.fetch_feed())

        # Collect posts from hashtags the user follows
        for entity in user.followed_entities:
            if isinstance(entity, Hashtag):  # Ensure we're working with hashtags
                user_feed.update(entity.posts)

        # Increment views for each post in the feed
        for post in user_feed:
            post.influencer.post_views[post.postId] += 1

        # Sort the combined feed by timestamp in descending order
        sorted_feed = sorted(user_feed, key=lambda post: post.timestamp, reverse=True)
        return sorted_feed

    def stats(self, entity_name, post_id=None):
        if entity_name in self.influencers:
            influencer = self.influencers[entity_name]
            if post_id:
                return influencer.post_views.get(post_id, 0)
            return influencer.get_stats()
        elif entity_name.startswith("#"):
            hashtag = self.hashtags.get(entity_name[1:])
            return len(hashtag.followers) if hashtag else 0

    def main(self):
        while True:
            try:
                command = input("Enter command: ").strip()
                if not command:
                    continue
                parts = command.split()
                action = parts[0]

                if action == "Create":
                    entity_type, name = parts[1], parts[2]
                    self.create_entity(entity_type, name)

                elif action == "Follow":
                    entity_name, user_name = parts[1], parts[2]
                    self.follow(entity_name, user_name)

                elif action == "Post":
                    influencer_name = parts[1]
                    message_parts = parts[2:]
                    message = []
                    hashtags = []
                    for part in message_parts:
                        if part.startswith("#"):
                            hashtags.append(part[1:])
                        else:
                            message.append(part)
                    self.post(influencer_name, " ".join(message), hashtags)

                elif action == "Fetch":
                    user_name = parts[1]
                    feed = self.fetch(user_name)
                    for post in feed:
                        print(f"Post Id {post.postId}: {post.influencer.name}: {post.message}")

                elif action == "Stats":
                    if parts[1].startswith("#"):
                        hashtag_name = parts[1]
                        print(self.stats(hashtag_name))
                    else:
                        influencer_name = parts[1]
                        if len(parts) > 2:
                            post_id = int(parts[2])
                            print(self.stats(influencer_name, post_id))
                        else:
                            followers, post_stats = self.stats(influencer_name)
                            print(f"Followers: {followers}")
                            print(f"Post Stats: {post_stats}")

                else:
                    print("Invalid command.")

            except EOFError:
                break
            except Exception as e:
                print(f"Error: {e}")


# Instantiate and run the feed system
instaFeed = InstagramFeed()
instaFeed.main()