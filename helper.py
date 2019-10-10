class Helper:
    def search_customer(participants):
        for p in participants:
            if "customer_appu-bxo0bgp6agfyrsof@qismo.com" in p["email"]:
                recipient_id = p["email"].split("_")[0]
                return recipient_id

        return None
