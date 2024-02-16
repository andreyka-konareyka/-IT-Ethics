def encrypt(m, key):
    return (m + key) % 256


def decrypt(m, key):
    return (m - key) % 256


def encrypt_data(data, key):
    return [encrypt(m, key) for m in data]

def decrypt_data(data, key):
    return [decrypt(m, key) for m in data]