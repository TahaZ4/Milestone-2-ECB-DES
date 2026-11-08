"""Appendix B - ECB pattern demonstration using OUR DES implementation."""
from des import ecb_encrypt
from common import SHARED_KEY

def show(label, text):
    ct = ecb_encrypt(text.encode(), SHARED_KEY)
    print(f"\n{label}\nPlaintext : {text!r}")
    for i in range(0, len(ct), 8):
        print(f"  Block {i//8+1}: {ct[i:i+8].hex().upper()}")
    return ct

ct = show("TEST 1 - two identical 8-byte blocks", "TRANSFERTRANSFER")
b = [ct[i:i+8] for i in range(0, 16, 8)]
print("\nBlock 1 == Block 2 ?", b[0] == b[1], "  <-- ECB leaks that the plaintext repeated")

ct2 = show("TEST 2 - same 8 bytes, but a different block in the middle", "TRANSFERPAYMENT$TRANSFER")
b2 = [ct2[i:i+8] for i in range(0, 24, 8)]
print("\nBlock 1 == Block 3 ?", b2[0] == b2[2], "  <-- identical even though the blocks are not neighbours")
