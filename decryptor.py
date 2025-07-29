import base64
from cryptography.fernet import Fernet

# Same key used in encryptor.py
key = b'TC_U05IK5xvT8O8IRRJZmAkIsxj0UULv5SCwnXghdQo='
cipher = Fernet(key)

def decrypt_log():
    with open("logs/exfiltrated_data.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        try:
            decoded = base64.b64decode(line)
            decrypted = cipher.decrypt(decoded).decode()
            print("\n🔓 Decrypted Log:\n", decrypted)
        except Exception as e:
            print("Error decrypting line:", e)

if __name__ == "__main__":
    decrypt_log()
