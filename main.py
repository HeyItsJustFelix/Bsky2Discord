import feedparser
from datetime import datetime, timedelta
import time
import sched
import requests
from config import servers, rss_feeds

global first_run
first_run = True

def get_feed(scheduler):
    global first_run
    scheduler.enter(60, 1, get_feed, (scheduler,))
    
    print("Checking for updates")

    for user in rss_feeds.get("feeds").values():
        url = user.get("feed")
        feed = feedparser.parse(url)
        post_link = feed.entries[0].link

        if user.get("last_post") != post_link:
            user.update({"last_post": post_link})

            fx_link = f"https://fx{post_link[8:]}"

            for server_name in user.get("servers"):
                webhook = servers["servers"][server_name]
                if not first_run:
                    webhook_data = {
                        "content": f"{webhook.get('role_ping')}\n[New post by {user.get('name')} on Bluesky!]({fx_link})"
                    }
                    result = requests.post(webhook.get("webhook_url"), json=webhook_data)
                    
                    try:
                        result.raise_for_status()
                    except requests.exceptions.HTTPError as err:
                        print(err)
                    else:
                        print(f"Payload delivered successfully, code {result.status_code}")

    first_run = False

my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(0, 1, get_feed, (my_scheduler,))
my_scheduler.run()