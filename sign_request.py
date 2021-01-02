import hashlib
import hmac
import base64

SECRET = bytes('█████', 'utf-8')


def get_message_for_request(request: str) -> bytes:
    # Parse the HTTP request.
    headers, body = request.split('\n\n', 1)

    method, path, _ = headers.split(' ', 2)

    # Drop the final newline from the body if needed.
    if body[-1] == '\n':
        body = body[:-1]

    headers = headers.split('\n')[1:]
    header_lookup = dict()
    for header in headers:
        name, value = header.split(': ', 1)
        header_lookup[name] = value

    # Compose the message.
    body_hashed = hashlib.sha256(body.encode('utf-8')).hexdigest()

    message = f'{method}\n{body_hashed}\n{header_lookup["Content-Type"]}\n{header_lookup["Date"]}\n{path}'

    return bytes(message, 'utf-8')


def entry() -> None:
    with open('request') as file:
        message = get_message_for_request(file.read())

    signature = base64.b64encode(hmac.new(SECRET, message, digestmod=hashlib.sha256).digest())

    print(f'X-Signature: HMAC widm-api:{signature.decode()}')


if __name__ == "__main__":
    entry()
