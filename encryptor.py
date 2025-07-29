from cryptography.fernet import Fernet

# You can generate your own key using Fernet.generate_key()
key = b'TC_U05IK5xvT8O8IRRJZmAkIsxj0UULv5SCwnXghdQo='
cipher = Fernet(key)

def encrypt_data(data):
    return cipher.encrypt(data.encode())
