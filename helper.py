import os
class Helper:
    def search_customer(participants):
        app_id = os.getenv("QISMO_APP_ID")
        for p in participants:
            if f"customer_{app_id}@qismo.com" in p["email"]:
                recipient_id = p["email"].split("_")[0]
                return recipient_id

        return None
