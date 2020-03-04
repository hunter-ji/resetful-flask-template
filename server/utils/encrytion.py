import hashlib
import base64
import json


def convert_to_md5(info):
    md5 = hashlib.md5()
    md5.update(info.encode('utf-8'))
    return md5.hexdigest()


def convert_to_base64(info):
    return base64.urlsafe_b64encode(json.dumps(info).encode())


def convert_to_text(info):
    return json.loads(base64.b64decode(info))


if __name__ == '__main__':
    text = { 'name': 'tom' }
    b6 = convert_to_base64(text)
    print('b6: ', b6)
    print('text: ', convert_to_text(b6)['name'])
