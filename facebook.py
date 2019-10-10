from pymessenger.bot import Bot
import requests
import os

FB_ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN")
FB_VERIFY_TOKEN = os.getenv("FB_VERIFY_TOKEN")
FB_GRAPH_URL = "https://graph.facebook.com/v2.6"
bot = Bot(FB_ACCESS_TOKEN)


class Facebook:
    def send_message(recipient_id, message):
        res = bot.send_text_message(recipient_id, message)
        if "error" in res:
            error_message = res["error"]["message"]
            raise Exception(f"Error while sending message to facebook: {error_message}")
        else:
            return "success"

    def verify_fb_token(token_sent, hub_challenge):
        if token_sent != FB_VERIFY_TOKEN:
            raise Exception("Invalid verification token")
        else:
            return hub_challenge

    def get_profile(user_id):
        url = f"{FB_GRAPH_URL}/{user_id}"
        query_string = {}
        query_string["access_token"] = FB_ACCESS_TOKEN

        res = requests.get(url, params=query_string)
        json_res = res.json()

        if res.status_code is not 200:
            error_message = json_res["error"]["message"]
            raise Exception(error_message)
        else:
            profile = {}
            profile["fullname"] = f"{json_res['first_name']} {json_res['last_name']}"
            profile["profile_pic"] = json_res["profile_pic"]
            return profile
