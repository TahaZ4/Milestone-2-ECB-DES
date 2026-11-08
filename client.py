"""Legacy Bank mobile app (Client): encrypts a test transaction with DES-ECB and sends it over TCP."""
import socket, struct
from des import ecb_encrypt
from common import SHARED_KEY, HOST, PORT

MESSAGE = "TXN#1042|FROM:ACC-1001|TO:ACC-2002|AMT:$500.00"

plaintext = MESSAGE.encode()
ciphertext = ecb_encrypt(plaintext, SHARED_KEY)
print(f"[CLIENT] Plaintext  : {MESSAGE}")
print(f"[CLIENT] Ciphertext : {ciphertext.hex().upper()}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(struct.pack("!I", len(ciphertext)) + ciphertext)   # length header + payload
    print("[CLIENT] Encrypted transaction sent.")
