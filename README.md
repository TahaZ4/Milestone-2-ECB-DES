# Milestone-2-ECB-DES
# Symetric Encryption Tunel (DES-ECB)

A secure comunication tunnel built for Legacy Bank, facilitating encrypted data exchnage between a mainframe server and a mobile client using Data Encription Standard (DES) in Electronic Codebook (ECB) mode.

---

## Features

- **Custom DES Implementation (`des.py`)**: Built from scratch to demonstrate the internal mecanics of a DES round, including Initial Permutations (IP), Fiestel rounds, S-boxes, and key scheduling.
- **TCP Socket Communicaiton**: Python-based client-server architechture handling message lenghts and byte streams over TCP sockets.
- **Cipher Security Analisys**: Comprehensive evalution comparing DES against classical ciphers (Ceasar, Substitution, Vigenère, Playfair, Hill, Transposition, Enigma) and documenting the inherent vulnerabilties of ECB mode.
- **Manual Hand-Calculation Apendix**: Step-by-step cryptographic walkthrough for a singel round of DES using test vectors (TRANSFER / LGCYBANK).

---

## Project Strucure

text
├── server.py             # Mainframe TCP server handling decrytpion
├── client.py             # Mobile app TCP client sending test transations
├── des.py                # Custom implemention of DES encryption/decryption
└── README.md             # Project documentaion and analysis report
