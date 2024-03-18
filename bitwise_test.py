byte_value = b'a'  # 这是一个ASCII码对应'd'字符的字节对象


# 提取第一个（也是唯一一个）字节，并进行按位取反

inv_byte = ~byte_value[0]


# Python内部自动处理了符号扩展，因此得到的结果仍是在0-255之间的数字

# 由于Python内建的int类型是足够大的，它能存储任何这样的小整数而无需担心溢出问题

unsigned_int = inv_byte & 0xFF  # 取模操作在这里其实是多余的，仅为了强调结果保持在8位无符号范围内


print(unsigned_int)

print(~unsigned_int & 0xFF)