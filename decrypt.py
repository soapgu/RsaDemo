from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

private_key = RSA.import_key(open("privateKey").read())
decipher_rsa = PKCS1_OAEP.new(private_key)
data_length = private_key.size_in_bytes();
print(f"私钥长度:{data_length}")

file_path = "cipher.data"
output_filename = "sample_restore.jpg"

with open(file_path, 'rb') as in_file:
    with open(output_filename, 'wb') as out_file:
        while content := in_file.read(data_length):  # 每次读取数据
            #print("---read data---")
            decrypted_chunk = decipher_rsa.decrypt(content)
            out_file.write(decrypted_chunk)

print("decrypt ok")