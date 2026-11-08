# Shared settings. In Milestone 2 the CTO wants a STATIC, HARDCODED 64-bit key.
# (8 ASCII characters = 64 bits. Note: DES only really uses 56 of them; every 8th bit is a parity bit.)
SHARED_KEY = b"LGCYBANK"          # hex: 4C 47 43 59 42 41 4E 4B
HOST, PORT = "127.0.0.1", 5050
