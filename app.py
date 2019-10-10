import json
from flask import Flask, request, jsonify
from qismo import Qismo as qismo
from facebook import Facebook as fb
from formatter import SuccessFomatter as success
from formatter import ErrorFormatter as error
from helper import Helper as helper
from werkzeug.exceptions import HTTPException


app = Flask(__name__)


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
                        if message["message"].get("text"):
                            text = message["message"].get("text")
                            qismo.send_message(recipient_id, text)
                        if message["message"].get("attachments"):
                            response_sent_nontext = get_message()
                            send_message(recipient_id, response_sent_nontext)

            success_message = "Success processing facebook message"
            app.logger.info(success_message)
            return (jsonify(success.message(success_message)), 200)
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

        text = output["payload"]["message"]["text"]
        fb.send_message(recipient_id, text)
        return jsonify(success.message("Success handling Qismo message")), 200
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(error.qismo_error(str(e))), 200


if __name__ == "__main__":
    app.run()

