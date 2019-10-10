import json
from flask import Flask, request, jsonify
from qismo import Qismo as qismo
from qiscus import Qiscus as qiscus
from facebook import Facebook as fb
from formatter import SuccessFomatter as success
from formatter import ErrorFormatter as error
from helper import Helper as helper
from werkzeug.exceptions import HTTPException


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    try:
        return jsonify(success.message("Success")), 200
    except expression as identifier:
        return jsonify(error.home_error(str(e))), 500


@app.route("/facebook-message", methods=["GET", "POST"])
def receive_message():
    try:
        if request.method == "GET":
            token_sent = request.args.get("hub.verify_token")
            hub_challenge = request.args.get("hub.challenge")

            verify_token = fb.verify_fb_token(token_sent, hub_challenge)
            return verify_token
        else:
            output = request.get_json()
            for event in output["entry"]:
                messaging = event["messaging"]
                for message in messaging:
                    if message.get("message"):
                        recipient_id = message["sender"]["id"]
                        profile = fb.get_profile(recipient_id)
                        fullname = profile["fullname"]

                        if message["message"].get("text"):
                            text = message["message"].get("text")
                            data = qismo.send_message(recipient_id, fullname, text)

                        if message["message"].get("attachments"):
                            message = message["message"]
                            attachments = message["attachments"]
                            attachment = attachments[0]
                            payload = attachment["payload"]
                            if payload is not None:
                                attachment_url = payload["url"]

                                if attachment_url is not None:
                                    data = qismo.send_attachment_message(
                                        recipient_id, fullname, attachment_url
                                    )

            success_message = "Success processing facebook message"
            app.logger.info(success_message)
            return jsonify(success.message(success_message)), 200
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(error.fb_error(str(e))), 200


@app.route("/qismo-message", methods=["POST"])
def qismo_message():
    try:
        output = request.get_json()
        participants = output["payload"]["room"]["participants"]

        recipient_id = helper.search_customer(participants)

        if recipient_id is None:
            raise Exception("Customer ID not found")

        # message_type = output["payload"]["message"]["type"]
        payload = output["payload"]
        message = payload["message"]
        message_type = message["type"]

        if message_type == "text":
            text = message["text"]
            fb.send_message(recipient_id, text)

        elif message_type == "file_attachment":
            attachment_payload = message["payload"]
            caption = attachment_payload["caption"]
            attachment_url = attachment_payload["url"]

            # !!!Send file like csv still error
            fb.send_attachment_message(recipient_id, attachment_url)

            if caption is not None or caption is not "":
                fb.send_message(recipient_id, caption)

        return jsonify(success.message("Success handling Qismo message")), 200
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(error.qismo_error(str(e))), 200


if __name__ == "__main__":
    app.run()

