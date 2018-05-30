import response

class PanOS_Request:

    def __init__(self):
        path = None
        payload = None

    def request(self):
        req = requests.get(path)
        response = response.Response(req)
        return response