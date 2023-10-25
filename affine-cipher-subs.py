# Extended Euclidean Algorithm untuk menemukan invers modulo
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

# Fungsi modinv untuk menghitung invers modulo
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None   # invers modulo tidak ada
    else:
        return x % m

# Fungsi enkripsi Affine Cipher kustom
# mengembalikan teks terenkripsi
def custom_affine_encrypt(text, key):
    """
    C = (a * P + b) % 26
    """
    alphabet = "qazplmnkoxswdcejbirhvuygft"
    return ''.join([alphabet[((key[0] * alphabet.index(t) + key[1]) % 26)] for t in text.lower() if t in alphabet])

# Fungsi dekripsi Affine Cipher kustom
# mengembalikan teks asli
def custom_affine_decrypt(cipher, key):
    """
    P = (a^-1 * (C - b)) % 26
    """
    alphabet = "qazplmnkoxswdcejbirhvuygft"
    return ''.join([alphabet[((modinv(key[0], 26) * (alphabet.index(c) - key[1])) % 26)] for c in cipher if c in alphabet])

# Fungsi untuk melakukan enkripsi atau dekripsi berdasarkan mode
def perform_custom_affine(text, key, mode):
    if mode == '1':
        return custom_affine_encrypt(text, key)
    elif mode == '2':
        return custom_affine_decrypt(text, key)
    else:
        return 'Pilihan tidak ada!'

# Driver Code untuk menguji fungsi-fungsi di atas
def main():
    while True:
        mode = input('1 untuk "enkripsi"\n2 untuk"dekripsi"\n0 untuk keluar\nmasukkan angka: ')
        
        if mode == '0':
            break
        elif mode != '1' and mode != '2':
            print('Pilihan tidak ada!')
            continue

        text = input('Masukkan teks: ')
        key = [7, 11]

        result = perform_custom_affine(text, key, mode)

        if result != 'Pilihan tidak ada!':
            print('Result: {}'.format(result))

if __name__ == '__main__':
    main()
