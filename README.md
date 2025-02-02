# X_bot

Objective: Automates various actions on the Twitter app using Appium for mobile automation.

Key Features:

Likes random tweets.
Posts comments on tweets.
Shares tweets via Direct Messages (DM).
Posts new tweets.
Sends direct messages to profiles.


Technologies Used:

Appium: For mobile automation and interaction with the Twitter Android app.
Python: Used for scripting the automation logic.
Appium Python Client: For interacting with Twitter's UI elements on the mobile app.
Appium Desktop Inspector: To look for the UI elements to be selected.

Modules:

like_tweet: Likes a randomly selected tweet.
comment_on_tweet: Posts a random comment on a selected tweet.
share_tweet_via_dm: Shares a tweet with a profile via DM.
send_direct_message: Sends a random DM to a profile.
post_tweet: Composes and posts a new tweet.

Main Control Flow:

The main.py script randomly selects and executes one of the actions (like, comment, share, send DM, or post).
Random Delays: Introduces random delays between actions to mimic human-like interaction.

The config.py file contains configuration settings for the Appium driver, including device details, app package, activity, and other capabilities necessary for interacting with the Twitter Android app. It is used to initialize the connection to the app during automation.

Purpose: Primarily designed for testing and automated interactions with the Twitter mobile app, simulating real-user behavior.
