from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import binascii


keys = '30980f98296b77f00a55f3c92b35322d898ae2ffcdb906de40336d2cf3d556a0'
iv = 'e5889166bb98ba01e1a6bc9b32dbf3e6'

def aes_string( input:str ):
    cipher = AES.new(binascii.unhexlify(keys), AES.MODE_CBC,iv=binascii.unhexlify(iv))
    decipher = AES.new(binascii.unhexlify(keys), AES.MODE_CBC,iv=binascii.unhexlify(iv))
    message = input.encode()
    pad_message = pad(message, AES.block_size)
    print(f"message:{message},pad message{pad_message}")
    text_secret = cipher.encrypt(pad_message)
    print(f"text_secret:{text_secret}")
    original_message = unpad(decipher.decrypt(text_secret),AES.block_size)
    print("Decrypted original message:", original_message)

aes_string('testtesttestte')

