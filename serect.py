import base64
import os
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

passsword = '1111'


# SUPPORT FUNCTION
def generate_key():
    binary_pass = passsword.encode('utf-8')
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, )
    key = base64.urlsafe_b64encode(kdf.derive(binary_pass))
    return key


def saveKey(key):
    key = key.decode('utf-8')
    file = open('Storage_Key.txt', 'a')
    file.write(key + '\n')


def getLis_Key():
    list_key = list()
    file = open('Storage_Key.txt', 'r')
    for key in file:
        key = key.strip()
        list_key.append(key)
    return list_key


# MAIN FUCTION
def encrypt(text):
    key = generate_key()
    saveKey(key)
    token = Fernet(key)
    text = text.encode('utf-8')
    return token.encrypt(text)


def decrypt(text):
    list_key = getLis_Key()
    for key in list_key:
        try:
            token = Fernet(key)
            result = token.decrypt(text)
            break
        except InvalidToken as err:
            continue
    return result.decode('utf-8')


def vertify(text):
    if text == passsword:
        return True
