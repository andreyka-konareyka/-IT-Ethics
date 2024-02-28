import affine
import read_write_file
import detectEnglish


def decrypt1():
    print('====  decrypt1  ====')
    encrypt_data = read_write_file.read_data_1byte('ff2_affine_c_all.bmp')
    a = 167
    b = 35
    l = 256
    a_inverse = affine.findModInverse(a, l)
    decrypt_data = []
    for e in encrypt_data:
        decrypt_data.append((e - b) * a_inverse % l)

    read_write_file.write_data_1byte('ff2_affine_c_all_decrypt.bmp', decrypt_data)
    print('\n')


def encrypt1():
    print('====  encrypt1  ====')
    data = read_write_file.read_data_1byte('ff2_affine_c_all.bmp')
    a = 167
    b = 35
    l = 256
    encrypt_data = data[:50]
    for m in data[50:]:
        encrypt_data.append((a * m + b) % l)
    read_write_file.write_data_1byte('ff2_affine_c_all_encrypt.bmp', encrypt_data)
    print('\n')


def decryptText():
    print('====  decryptText  ====')
    encrypt_data = read_write_file.read_data_1byte('text10_affine_c_all.txt')
    l = 256

    for a in range(1, 256):
        for b in range(256):
            a_inverse = affine.findModInverse(a, l)
            if a_inverse is None:
                continue
            decrypt_data = []
            for e in encrypt_data:
                decrypt_data.append((e - b) * a_inverse % l)

            txt = ''.join([chr(s) for s in decrypt_data])
            if detectEnglish.isEnglish(txt):
                print(f'Key found => a = {a}, b = {b}')
                print(f'test = {txt}')
                print('\n')
                return
    print('Key not found')
    print('\n')


if __name__ == '__main__':
    decrypt1()
    encrypt1()
    decryptText()
