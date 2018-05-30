#!/usr/bin/python3

import asyncio
import requests
import panos_request

host = '192.168.15.9'
apikey = ''

def main()
    req = panos-request.PanOS_Request()
    req.key = apikey
    req.path = 'https://{url}/api/?type=op&cmd=<show><system><info></info></system></show>&key={apikey}'.format(url, apikey)

    resp = req.request()
    print(resp.text)

if __name__ == 'main':
    main()