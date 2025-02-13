# Your User class goes here
class User:
    posts = []

    def __init__(self, name, email, drivers_license, User_posts=None):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license
        # set default as None - otherwise if you set it as init(posts = []) ->
        # any changes to posts in one instance will be shared across ALL instances
        if User_posts is None:
            User_posts = []
        self.User_posts = User_posts
    
    ###############
    # Prints all global posts
    def see_all_posts(self):
        # if this False check wasn't there, it would return '[]' ->
        # which would fail the test - it has to return None (blank)
        if not User.posts:
            return None
        else:
            print(User.posts)
    # Prints users local posts
    def see_my_posts(self):
        if not self.User_posts:
            return None
        else:
            print(self.User_posts)
    # Prints local user info more for us as a developer
    def __repr__(self):
        return f"{self.name} | {self.email} | {self.drivers_license} | {self.User_posts}"
    ###############

    def create_a_post(self):
        new_post_title = input("What would you like the title to be?: ")
        new_post_body = input("What would you like to post?: ")
        # setting a post ID so deleting the post becomes easier ->
        # post ID will check the length of the global User Posts & set it to that + 1
        # must convert post id to a str because dict keys have to be a string, not int
        post_id = str(len(User.posts)+1)
        # Add the new post to both global posts and personal posts 
        #  format = post id  :   post title   ,  post body
        new_post = {post_id: [new_post_title, new_post_body]}
        self.User_posts.append(new_post)
        self.posts.append(new_post)
        # Now we need to get whoever is the current user,
        # and add that post to their local posts
        print("Posted!")

    def delete_a_post(self):
        post_to_delete = str(input("What is the ID of the post you'd like to delete?: "))
        # Go into global post list and look at each indexes key (the post_id)
        # for each index in User.User_posts list
        for id in User.posts:
            if post_to_delete in id:
         # going to list of All posts @ the index of the current post we're at in our loop
                del User.posts[User.posts.index(id)]
         # going to local user post lists at the same index as above since ->
         # the post is in both post lists
                del self.User_posts[self.User_posts.index(id)]

# chase = FreeUser("chase", 'chase@chase.com', 123)
# chase.create_a_post()
# chase.create_a_post()
# chase.see_my_posts()
# chase.see_all_posts()
# chase.create_a_post()
# chase.delete_a_post()
# chase.see_all_posts()
# chase.see_my_posts()
# chase.create_a_post()
# chase.see_my_posts()
# chase.see_all_posts()
