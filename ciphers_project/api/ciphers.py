
def caesar_encode(plain_text, shift):
    cipher_text = ""
    if shift < 0:
        shift = shift + 26
    for c in plain_text:    
        c_encoded = ord(c) + shift
        c_encoded = chr(c_encoded)
        cipher_text += c_encoded
    return cipher_text