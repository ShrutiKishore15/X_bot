import random
from actions.like_tweet import like_tweet
from actions.comment_on_tweet import comment_on_tweet
from actions.post_tweet import post_tweet
from actions.share_tweet_via_dm import share_tweet_via_dm
from actions.send_direct_message import send_direct_message
from actions.navigate_to_home import navigate_to_home
import time

# Random delay function
def random_delay():
    delay = random.randint(0, 10)
    print(f"Waiting for {delay} seconds.")
    time.sleep(delay)

try:
    actions = [like_tweet, comment_on_tweet, post_tweet, share_tweet_via_dm]
    for _ in range(10):  # Perform 10 random actions
        action = random.choice(actions)
        action()  # Execute the randomly chosen action
        random_delay()  # Wait for a random time between actions
finally:
    # Ensure the driver quits at the end of the script
    from config import driver
    driver.quit()
