"""Appendix A helper: prints every intermediate value of DES round 1 for plaintext 'TRANSFER', key 'LGCYBANK'."""
from des import *
s = lambda b, n=0: "".join(map(str, b)) if not n else " ".join("".join(map(str, b[i:i+n])) for i in range(0, len(b), n))
key, pt = b"LGCYBANK", b"TRANSFER"
print("KEY  ascii/hex/bin:", key, key.hex().upper(), s(bytes_to_bits(key), 8))
print("PT   ascii/hex/bin:", pt, pt.hex().upper(), s(bytes_to_bits(pt), 8))
k56 = permute(bytes_to_bits(key), PC1); c0, d0 = k56[:28], k56[28:]
print("\nPC-1 (56b):", s(k56, 7)); print("C0:", s(c0, 7)); print("D0:", s(d0, 7))
c1, d1 = rotl(c0, 1), rotl(d0, 1)
print("C1 (rot 1):", s(c1, 7)); print("D1 (rot 1):", s(d1, 7))
K1 = permute(c1 + d1, PC2); print("K1 (PC-2, 48b):", s(K1, 6)); print("K1 hex:", bits_to_bytes(K1 + [0]*0 if False else K1).hex().upper() if len(K1)%8==0 else hex(int(s(K1),2)))
ip = permute(bytes_to_bits(pt), IP); L0, R0 = ip[:32], ip[32:]
print("\nAfter IP :", s(ip, 8)); print("L0:", s(L0, 8)); print("R0:", s(R0, 8))
eR = permute(R0, E); print("\nE(R0) 48b:", s(eR, 6))
x = xor(eR, K1); print("E(R0) xor K1:", s(x, 6))
out = []
for i in range(8):
    six = x[6*i:6*i+6]; r, c, v = sbox_lookup(six, i)
    print(f"S{i+1}: in={s(six)}  row=(b1,b6)={six[0]}{six[5]}={r}  col=(b2-b5)={s(six[1:5])}={c}  -> S{i+1}[{r}][{c}] = {v} = {v:04b}")
    out += [(v >> (3-j)) & 1 for j in range(4)]
print("\nS-box output (32b):", s(out, 4))
f = permute(out, P); print("After P  f(R0,K1):", s(f, 4))
R1 = xor(L0, f); L1 = R0
print("\nL1 = R0         :", s(L1, 8)); print("R1 = L0 xor f   :", s(R1, 8))
print("L1 hex:", bits_to_bytes(L1).hex().upper(), " R1 hex:", bits_to_bytes(R1).hex().upper())
print("\nFull 16-round ciphertext of 'TRANSFER':", encrypt_block(pt, key).hex().upper())
