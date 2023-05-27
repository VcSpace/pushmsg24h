from Crypto.Cipher import AES
from binascii import hexlify
import os

# 生成16字节的随机密钥
key = os.urandom(16)
# 生成16字节的随机偏移位
iv = os.urandom(16)
# 将密钥和偏移位转换为十六进制字符串
key_hex = hexlify(key)
iv_hex = hexlify(iv)[:16] # 只取前16个字符
print("key:", key_hex)
print("iv:", iv_hex)
