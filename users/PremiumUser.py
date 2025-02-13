# Your PremiumUser class goes here
from user import User

class PremiumUser(User):
    def __init__(self, name, email, drivers_license, User_posts=None):
        super().__init__(name, email, drivers_license, User_posts=None)

# chase = PremiumUser("chase", 'chase@chase.com', 123)
# chase.create_a_post()
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