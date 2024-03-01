import cesar
import read_write_file
import detectEnglish
import substitution


def test1():
    print('====  test1  ====')
    m = 24
    key = 37
    c = cesar.encrypt(m, key)
    print(f"c = {c}")

    m1 = cesar.decrypt(c, key)
    print(f"m1 = {m1}")


    data = [34, 67, 123, 79, 201]
    enc_data = cesar.encrypt_data(data, key)
    print(f"encrypt_data = {enc_data}")

    dec_data = cesar.decrypt_data(enc_data, key)
    print(f"encrypt_data = {dec_data}")

    data = read_write_file.read_data_1byte("f1.txt")
    print(f"data = {data[0:15]}")

    txt = ''
    for n in data[0:15]:
        txt += chr(n)

    print(f'text = {txt}')
    print('\n')


def encrypt1():
    print('====  encrypt1  ====')
    data = read_write_file.read_data_1byte("f1.txt")
    print(f"data = {data[0:15]}")

    encrypt_data = cesar.encrypt_data(data, key=67)
    print(f'encript_data = {encrypt_data[0:15]}')

    txt = ''.join([chr(s) for s in encrypt_data[0:15]])
    print(f'encript_text = {txt}')

    read_write_file.write_data_1byte('f1_encrypt.txt', encrypt_data)
    print('\n')


def decrypt1():
    print('====  decrypt1  ====')
    encrypt_data = read_write_file.read_data_1byte('f1_encrypt.txt')
    print(f'encrypt_data = {encrypt_data[0:15]}')

    decrypt_data = cesar.decrypt_data(encrypt_data, key=67)
    print(f'decrypt_data = {decrypt_data[0:15]}')

    txt = ''.join([chr(s) for s in decrypt_data[0:15]])
    print(f'decrypt_text = {txt}')

    read_write_file.write_data_1byte('f1_decrypt.txt', decrypt_data)
    print('\n')


def decryptUnknowText():
    print('====  decryptUnknowText  ====')
    encrypt_data = read_write_file.read_data_1byte('t3_caesar_c_all.txt')
    print(f'encrypt_data = {encrypt_data[0:15]}')
    for k in range(256):
        # расшифровываем
        decrypt_data = cesar.decrypt_data(encrypt_data, key=k)
        # смотрим, что получилось
        txt = ''.join([chr(s) for s in decrypt_data])
        # print(f'decrypt_data=', txt)
        # проверяем, полученный текст - английский или нет
        is_english = detectEnglish.isEnglish(txt)
        if is_english:
            print(txt)
            print(f'Key found = {k}')
            print('\n')
            return
    print('404. Key not found')
    print('\n')


def encryptImage():
    print('====  encryptImage  ====')
    data = read_write_file.read_data_1byte('f2.png')
    encrypt_data = cesar.encrypt_data(data, key=143)
    read_write_file.write_data_1byte('f2_encrypt.png', encrypt_data)
    print('\n')


def decryptImage():
    print('====  decryptImage  ====')
    encrypt_data = read_write_file.read_data_1byte('f2_encrypt.png')
    for k in range(256):
        decrypt_data = cesar.decrypt_data(encrypt_data[0:2], key=k)

        if decrypt_data[0] == int('89', 16) and decrypt_data[1] == int('50', 16):
            print(f'Key found = {k}')
            print('\n')
            return
    print('404. Key not found')
    print('\n')


def testDecryptN2():
    print('====  testDecryptN2  ====')
    encrypt_data = read_write_file.read_data_1byte('t3_caesar_c_all.txt')
    print(f'encrypt_data = {encrypt_data[0:15]}')
    for k in range(256):
        # расшифровываем
        decrypt_data = cesar.decrypt_data(encrypt_data, key=k)
        # смотрим, что получилось
        txt = ''.join([chr(s) for s in decrypt_data])
        print(f'decrypt_data=', txt)
        # проверяем, полученный текст - английский или нет
        is_english = detectEnglish.isEnglish(txt)
        if is_english:
            print(f'Key found = {k}')
            print(f'text = {txt}')
            print('\n')
            return
    print('404. Key not found')
    print('\n')


def decryptWithTable():
    print('====  decryptWithTable  ====')
    encrypt_data = read_write_file.read_data_1byte('c3_subst_c_all.png')
    decrypt_data = substitution.decrypt(encrypt_data)
    read_write_file.write_data_1byte('c3_subst_c_all_decrypt.png', decrypt_data)
    print('\n')


if __name__ == '__main__':
    # test1()
    # encrypt1()
    # decrypt1()
    decryptUnknowText()
    # encryptImage()
    # decryptImage()
    # testDecryptN2()
    # decryptWithTable()
