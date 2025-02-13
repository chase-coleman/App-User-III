from user import User

class FreeUser(User):
    def __init__(self, name, email, drivers_license, User_posts=None):
        super().__init__(name, email, drivers_license, User_posts=None)
        
    
    def create_a_post(self):
        # Checks if the users posts is 0 or 1 -> if yes, they can post again
        # if no, they've already posted twice, and must upgrade
        if len(self.User_posts) in range(0,2):
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
        else: print("You've reach your post limit. To make another post, upgrade to Premium.")

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