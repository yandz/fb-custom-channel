import requests
import os

QISMO_IDENTIFIER_KEY = os.getenv("QISMO_IDENTIFIER_KEY")
QISMO_BASE_URL = os.getenv("QISMO_BASE_URL")
QISMO_APP_ID = os.getenv("QISMO_APP_ID")


class Qismo:
    def send_message(user_id, fullname, message):
        data = {}
        data["identifier_key"] = QISMO_IDENTIFIER_KEY
        data["user_id"] = f"{user_id}_customer_{QISMO_APP_ID}@qismo.com"
        data["name"] = fullname
        data["message"] = message

        url = f"{QISMO_BASE_URL}/{QISMO_APP_ID}/custom_channel"
        res = requests.post(url, data=data)

        if res.status_code is not 200:
            raise Exception("Sending message to Qismo Failed")
        else:
            json_res = res.json()
            data = json_res["data"]

            return data

    def send_attachment_message(user_id, fullname, attachment_url):
        data = {}
        data["identifier_key"] = QISMO_IDENTIFIER_KEY
        data["user_id"] = f"{user_id}_customer_{QISMO_APP_ID}@qismo.com"
        data["name"] = fullname
        data["message"] = f"[file]{attachment_url}[/file]"

        url = f"{QISMO_BASE_URL}/{QISMO_APP_ID}/custom_channel"
        res = requests.post(url, data=data)

        if res.status_code is not 200:
            raise Exception("Sending message to Qismo Failed")
        else:
            json_res = res.json()
            data = json_res["data"]

            return data
