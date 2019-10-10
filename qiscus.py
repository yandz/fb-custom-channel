import requests
import os

QISCUS_BASE_URL = os.getenv("QISCUS_BASE_URL")
QISCUS_SDK_APP_ID = os.getenv("QISCUS_SDK_APP_ID")
QISCUS_SDK_SECRET = os.getenv("QISCUS_SDK_SECRET")


class Qiscus:
    def update_room_avatar(room_id, avatar_url):
        url = f"{QISCUS_BASE_URL}/api/v2.1/rest/update_room"
        headers = {}
        headers["QISCUS_SDK_SECRET"] = QISCUS_SDK_SECRET
        headers["QISCUS_SDK_APP_ID"] = QISCUS_SDK_APP_ID

        payload = {}
        payload["room_id"] = room_id
        payload["room_channel_id"] = str(room_id)
        payload["room_avatar_url"] = avatar_url

        res = requests.post(url, headers=headers, data=payload)

        if res.status_code is not 200:
            raise Exception("Failed updating room avatar url")
        else:
            return "success"
