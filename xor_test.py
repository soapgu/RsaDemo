from itertools import cycle

def xor_cipher(text, key):
    encrypted_text = bytes([(c^k) for c, k in zip(text, cycle(key))])
    return encrypted_text

def xor_decipher(encrypted_text, key):
    # 加密和解密使用的是同一函数，因为异或运算具有相反可逆性
    return xor_cipher(encrypted_text, key)

plaintext = b"Hello, World!"

key = b'shgbit'


encrypted = xor_cipher(plaintext, key)
print("Encrypted Text:", encrypted)
decrypted = xor_decipher(encrypted, key)
print("Decrypted Text:", decrypted)