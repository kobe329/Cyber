import base64
KEY = 201  # "ключ" шифрования, можно поменять на любое число 0–255

def encrypt(text: str) -> str:
    data = text.encode("utf-8")
    xored = bytes(b ^ KEY for b in data)
    return base64.urlsafe_b64encode(xored).decode("ascii")