from urllib import request
from urllib.error import HTTPError, URLError
import ssl
import json

def rpc_request(method, params):
    url = "https://slb.medv.ru/api/v2/"
    payload = {"method": method, "params": list(params), "jsonrpc": "2.0", "id": 0}

    req = request.Request(url)
    req.add_header("content-type", "application/json")

    data = json.dumps(payload)
    data = data.encode()

    context = ssl.create_default_context()
    context.load_cert_chain(certfile="client.crt", keyfile="client.key")

    try:
        r = request.urlopen(req, data=data, context=context)
        content = r.read()
        return content
    
    except HTTPError as e:
        print(f"HTTP Error: {e.code}")
    except URLError as e:
        print(f"URL Error: {e.reason}")