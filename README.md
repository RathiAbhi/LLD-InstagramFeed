Instagram Feed
Problem statement

We would like to design the instagram feed which will have two actors i.e. Influencers and
Users.
Influencers can create content for the users to watch. They can use hashtags in their posts to
increase their reach.
Users can subscribe to both Influencers or hashtags.
Following stories are in the scope of the MVP:
- Can create an Influencer
- Can delete an Influencer
- Influencers can create a post. If a post has a new hashtag created then we should
register a new hashtag and send the post to all the followers of influencer/hashtags.
- Influencers can delete a post. No users will be able to see this post.
- Influencers can see stats for number of followers and number of views on a particular
post. 
- Can create/delete an user.
- Can follow/unfollow an influencer or a hashtag.
- Users can call fetch feed to receive the feed. Feed should be in decreasing order of
creation timestamp.
- If the number of followers > 3 then post the new post to user feed at time of creation
otherwise add it to user feed on demand.

Input
- Create <Actor> <Name>
- Follow <Influencer/Hashtag> <User>
- Post <Influencer> <MSG> ... [<Hashtag>]
- Fetch <User>
- Stats <Influencer/Hashtag> #number of followers
- Stats <Influencer> <PostId> #number of views

Example
- Create Influencer Samay
- Create User RK
- Create User JSP
- Create User AJ
- Follow Samay RK
- Post Samay “This is sparta” #war
- Follow #war RK
- Fetch RK
- Post Id 1: Samay: “This is Sparta”
- Create Influencer AIB
- Follow AIB JSP
- Follow AIB AJ
- Post AIB “A King may move a man, a father may claim a son, that man can also move
himself, and only then does that man truly begin his own game” #war
- Fetch RK
- Post Id 1: Samay: “This is Sparta”
- Post Id 2: AIB : “A King may move a man, a father may claim a son, that man can
also move himself, and only then does that man truly begin his own game”
- Stats AIB
- 2
- Follow AIB RK
- Stats Samay
- 1
- Stats AIB
- 3
- Stats AIB PostId2
- 1
