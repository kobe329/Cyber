from encrypt import encrypt
from decrypt import decrypt

if __name__ == "__main__":
    print("Что шифруем / расшифровываем?")
    word = input()

    print("Что делаем? \n 1 - секрет (зашифровать) \n 2 - не секрет (расшифровать)")
    chosen_num = int(input())

    if chosen_num == 1:
        print("Зашифровано:")
        print(encrypt(word))

    elif chosen_num == 2:
        print("Расшифровано:")
        print(decrypt(word))
