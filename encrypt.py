from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

recipient_key = RSA.import_key(open("publicKey").read())
max_plain_text_len = recipient_key.size_in_bytes() - 42 
print(f"使用此密钥进行RSA加密时，最大明文长度是 {max_plain_text_len} 字节")
cipher_rsa = PKCS1_OAEP.new(recipient_key)

file_path = "sample.jpg"
output_filename = "cipher.data"
with open(file_path, 'rb') as in_file:
    with open(output_filename, 'wb') as out_file:
        while content := in_file.read(max_plain_text_len):  # 每次读取数据
            #print("---read data---")
            encrypted_chunk = cipher_rsa.encrypt(content)
            out_file.write(encrypted_chunk)

file_length = os.path.getsize(output_filename)
print(f"cipher file size:{file_length}")
