import hashlib
import base64 
def encodeBase64(string):
    sample_string = str(string)
    sample_string_bytes = sample_string.encode("ascii") 
    base64_bytes = base64.b64encode(sample_string_bytes) 
    return base64_bytes.decode("ascii") 
def decodeBase64(string):
    base64_string =string
    base64_bytes = base64_string.encode("ascii") 
    sample_string_bytes = base64.b64decode(base64_bytes) 
    return sample_string_bytes.decode("ascii") 
def hashMD5(value):
    return hashlib.md5(value.encode('utf-8')).hexdigest()
def sha256(value):
    return hashlib.sha256(value.encode()).hexdigest()


