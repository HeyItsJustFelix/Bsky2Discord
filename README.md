# Bsky2Discord
A simple program to check bluesky RSS feeds every minute, and send new posts using fxbsky urls to Discord

# Instructions
## Creating a Webhook
To create a webhook, enter the settings of the Discord channel you want Bluesky posts to be sent to, go to the integrations tab, click Create Webhook. If the channel already has a webhook, click New Webhook. Rename the newly created webhook to anything, I personally name it Bluesky and add the Bluesky logo as the pfp. Copy the webhook url, and save this for later

## Getting an RSS Feed from Bluesky
Go to the profile of the user you want to track in the browser, add /rss at the end of the url, and hit enter. This should change the url from https://bsky.app/profile/itsjustfelix.felixbot.io to the more permanant url of https://bsky.app/profile/did:plc:kuizmkkzuourkemhynr3nqrm/rss. Copy this URL and save it for later

## Setting up the Code
Download and unzip the code. Inside of the folder you just extracted, edit the config.py file, and make a new entry following the example in the comments of the file.

Once you have configured the code, we need to set up a python instance with the proper packages

## Running the Code
I have not tested this code on anything older than Python 3.10, although this should hopefully work on older versions.

### Windows Specific Instructions
If you do not have python already, I recommend installing Python 3.10 or newer. I highly recommend checking "Add to PATH" during installation so you don't have to reference to the file location. Once you have Python installed, make sure that you're inside of the folder with the code by typing `cmd` at the top of the file explorer window. Once the command prompt is open, run `python.exe -m venv env`, then run `.\env\Scripts\activate`. This will put you into an environment where you can install packages locally. Next, run `python.exe -m pip install -r requirements.txt` to install the required packages for the bot.

Once you have your venv set up properly, you should be able to run `python.exe main.py` to run the code!

### Windows troubleshooting
If you receive `python.exe not found` or something similar, please rerun the installer, click modify, and click next, and make sure that `Add python to environment variables` is checked, then click Install.

### Linux specific instructions
If you do not have python already, I recommend installing Python 3.10 or newer. Once you have Python installed, run `python3 -m venv env`, then run `source ./env/bin/activate`. This will put you into an environment where you can install packages locally. Next, run `python -m pip install -r requirements.txt` to install the required packages for the bot.

Once you have your venv set up properly, you should be able to run `python main.py` to run the code!