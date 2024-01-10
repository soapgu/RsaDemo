from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes
import time
import os

BLOCK_SIZE = 32

aes_key = open("aes_key","rb").read()
aes_iv = open("aes_iv","rb").read()

#cipher_aes = AES.new(aes_key, AES.MODE_CTR,nonce=aes_iv)
decipher_aes = AES.new(aes_key, AES.MODE_ECB)

text_secret = open("string.data","rb").read()
print(text_secret)
original_message = decipher_aes.decrypt(text_secret)
print("Decrypted original message:", original_message)

original_message = decipher_aes.decrypt(text_secret)
print("Decrypted original message:", original_message)

# org_file = decipher_aes.decrypt(file_in)
# print( org_file )
# org_file = decipher_aes.decrypt(file_in)
# print( org_file )
# org_file = decipher_aes.decrypt(file_in)
# print( org_file )

'''
file = "16710673437381651.jpg"
download_path = os.path.join(os.getcwd(), "downloads" , file)
#output_filename = os.path.join(os.getcwd(), "downloads" , "aes_"+file)
output_filename = "sample_restore1.jpg"
count = 0
with open(download_path, 'rb') as in_file:
    with open(output_filename, 'wb') as out_file:
        while content := in_file.read(BLOCK_SIZE):  # 每次读取数据
            decrypted_chunk = decipher_aes.decrypt(content)
            out_file.write(decrypted_chunk)
            if(count == 1):
                print(content)
                print(decrypted_chunk)
            count = count + 1
            #print(f"计数{count},length:{len(decrypted_chunk)}")
'''