class Response:

    class __init__(self, resp):
        self.response_code = resp.status_code
        self.text = resp.text