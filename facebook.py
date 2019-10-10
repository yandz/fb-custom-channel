from pymessenger.bot import Bot
import os

FB_ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN")
FB_VERIFY_TOKEN = os.getenv("FB_VERIFY_TOKEN")
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
        pass
