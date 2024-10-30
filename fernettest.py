from cryptography.fernet import Fernet

key = b'TQenjgBHJFv6Ep4v8eN0Bayf194BS6qV_X23n5ulnRQ='
f = Fernet(key)


s = "test"

enc = f.encrypt(bytes(s.encode()))
dec = f.decrypt(bytes(enc))
print(f, enc, str(dec, 'UTF-8'))