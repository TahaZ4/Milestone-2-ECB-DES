"""Legacy Bank mainframe (Server): receives a DES/ECB-encrypted transaction, decrypts and prints it."""
import socket, struct
from des import ecb_decrypt
from common import SHARED_KEY, HOST, PORT

def recv_exact(conn, n):
    """TCP is a byte stream, not a message stream, so keep reading until we have n bytes."""
    buf = b""
    while len(buf) < n:
        chunk = conn.recv(n - len(buf))
        if not chunk:
            raise ConnectionError("client closed the connection early")
        buf += chunk
    return buf

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, PORT))
    srv.listen(1)
    print(f"[SERVER] Mainframe listening on {HOST}:{PORT} ...")
    conn, addr = srv.accept()
    with conn:
        print(f"[SERVER] Mobile app connected from {addr}")
        length = struct.unpack("!I", recv_exact(conn, 4))[0]     # 4-byte length header
        ciphertext = recv_exact(conn, length)
        print(f"[SERVER] Ciphertext received ({length} bytes): {ciphertext.hex().upper()}")
        plaintext = ecb_decrypt(ciphertext, SHARED_KEY)
        print(f"[SERVER] Decrypted transaction : {plaintext.decode()}")
