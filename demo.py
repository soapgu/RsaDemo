from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

recipient_key = RSA.import_key(open("publicKey").read())
max_plain_text_len = recipient_key.size_in_bytes() - 42 
print(f"使用此密钥进行RSA加密时，最大明文长度是 {max_plain_text_len} 字节")
cipher_rsa = PKCS1_OAEP.new(recipient_key)
message = b'This is a secret message to be encrypted,This is a secret message to be encrypted,This'
print(f"当前长度{len(message)}")
ciphertext = cipher_rsa.encrypt(message)
print("Ciphertext:", ciphertext)
print(len(ciphertext))

private_key = RSA.import_key(open("privateKey").read())
decipher_rsa = PKCS1_OAEP.new(private_key)
original_message = decipher_rsa.decrypt(ciphertext)
print(len(original_message))
print("Decrypted original message:", original_message.decode('utf-8'))