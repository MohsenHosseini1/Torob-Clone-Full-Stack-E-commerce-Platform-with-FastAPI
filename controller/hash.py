import hashlib
def hash_passwd(password):
    return hashlib.md5(password.encode()).hexdigest()