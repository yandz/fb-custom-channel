class SuccessFomatter:
    def message(message):
        response_data = {}
        response_data["code"] = 200
        response_data["message"] = message

        return response_data


class ErrorFormatter:
    def fb_error(message):
        response_data = {}
        response_data["code"] = 500
        response_data["error"] = {}
        response_data["error"]["message"] = message
        response_data["error"]["type"] = "FacebookMessageHandlerError"

        return response_data

    def qismo_error(message):
        response_data = {}
        response_data["code"] = 500
        response_data["error"] = {}
        response_data["error"]["message"] = message
        response_data["error"]["type"] = "QismoMessageHandlerError"

        return response_data

    def home_error(message):
        response_data = {}
        response_data["code"] = 500
        response_data["error"] = {}
        response_data["error"]["message"] = message
        response_data["error"]["type"] = "HomeError"

        return response_data
