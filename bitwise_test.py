byte_value = b'a'  # 这是一个ASCII码对应'a'字符的字节对象

def bitwise_not_encrypt( input : int ):
    print(f"input byte:{input}")
    output = ~input & 0xFF
    # Python内部自动处理了符号扩展，因此得到的结果仍是在0-255之间的数字
    # 由于Python内建的int类型是足够大的，它能存储任何这样的小整数而无需担心溢出问题
    print(f"output byte:{output}")
    return output

# 提取第一个（也是唯一一个）字节，并进行按位取反
print("encrypt>>>>>>>")
encrypt = bitwise_not_encrypt(byte_value[0])
print("decrypt>>>>>>>")
decrypt = bitwise_not_encrypt(encrypt)

