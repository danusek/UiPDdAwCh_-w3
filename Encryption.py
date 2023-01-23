import codecs

def encrypt_base64(text):
    return codecs.encode(text.encode(), 'base64').decode().strip()

def decrypt_base64(enc_text):
    return codecs.decode(enc_text.encode(), 'base64').decode()

text = "To jest haslo do zaszyfrowania"
enc_text = encrypt_base64(text)
print("Zaszyfrowane: ", enc_text)
dec_text = decrypt_base64(enc_text)
print("Bez szyfrowania: ", dec_text)