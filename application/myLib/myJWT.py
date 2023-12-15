import hmac
import base64
import json
import hashlib
def decode(token,key):
    header_encoded,payload_encoded,signature = token.split(".") 
    header = json.loads(base64.urlsafe_b64decode(header_encoded))
    payload = json.loads(base64.urlsafe_b64decode(payload_encoded))
    return {
        "header": header,
        "payload": payload
    }
