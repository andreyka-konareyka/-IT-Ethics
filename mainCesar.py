from cesar import encrypt, decrypt, encrypt_data, decrypt_data
import read_write_file


def main():

    m = 24
    key = 37
    c = encrypt(m, key)
    print(f"c = {c}")

    m1 = decrypt(c, key)
    print(f"m1 = {m1}")


    data = [34, 67, 123, 79, 201]
    enc_data = encrypt_data(data, key)
    print(f"encrypt_data = {enc_data}")

    dec_data = decrypt_data(enc_data, key)
    print(f"encrypt_data = {dec_data}")

    data = read_write_file.read_data_1byte("f1.txt")
    print(f"data = {data[0:15]}")

if __name__ == '__main__':
    main()