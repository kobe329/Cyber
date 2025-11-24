import base64
KEY = 201  # "ключ" шифрования, можно поменять на любое число 0–255

def decrypt(encoded: str) -> str:
    # обратно из base64 в байты
    data = base64.urlsafe_b64decode(encoded.encode("ascii"))
    # снимаем XOR
    xored = bytes(b ^ KEY for b in data)
    # обратно в строку
    return xored.decode("utf-8")
