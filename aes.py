from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes
import time

BLOCK_SIZE = 16 * 1024

print("begin to encrypt...")

data = 'secret data to transmit'.encode()

aes_key = open("aes_key","rb").read()
aes_iv = open("aes_iv","rb").read()

print(aes_key)
print(aes_iv)
cipher = AES.new(aes_key, AES.MODE_CTR,nonce=aes_iv)
ciphertext = cipher.encrypt(data)

print("Ciphertext:", ciphertext)

open("string.data","wb").write(ciphertext)

decipher = AES.new(aes_key, AES.MODE_ECB,nonce=aes_iv)
original_message = decipher.decrypt( ciphertext )
print("Decrypted original message:", original_message.decode('utf-8'))


start_time = time.time()
file_path = "sample.jpg"
output_filename = "downloads/16710673437381651.jpg"
with open(file_path, 'rb') as in_file:
    with open(output_filename, 'wb') as out_file:
        while content := in_file.read(BLOCK_SIZE):  # 每次读取数据
            #print("---read data---")
            encrypted_chunk = cipher.encrypt(content)
            out_file.write(encrypted_chunk)

end_time = time.time()
run_time = end_time - start_time
print(f"加密运行时间: {run_time} 秒")


file_path = "downloads/16710673437381651.jpg"
output_filename = "sample_restore1.jpg"
count = 0
with open(file_path, 'rb') as in_file:
    with open(output_filename, 'wb') as out_file:
        while content := in_file.read(BLOCK_SIZE):  # 每次读取数据
            #print("---read data---")
            
            decrypted_chunk = decipher.decrypt(content)
            out_file.write(decrypted_chunk)
            count = count + 1
            #print(f"计数{count},length:{len(decrypted_chunk)}")
print("decrypt ok")
