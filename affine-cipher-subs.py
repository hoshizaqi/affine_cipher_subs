# Extended Euclidean Algorithm for finding modular inverse
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

# Custom affine cipher encryption function
# returns the cipher text
def custom_affine_encrypt(text, key):
    """
    C = (a * P + b) % 26
    """
    alphabet = "qazplmnkoxswdcejbirhvuygft"
    return ''.join([alphabet[((key[0] * alphabet.index(t) + key[1]) % 26)] for t in text.lower() if t in alphabet])

# Custom affine cipher decryption function
# returns the original text
def custom_affine_decrypt(cipher, key):
    """
    P = (a^-1 * (C - b)) % 26
    """
    alphabet = "qazplmnkoxswdcejbirhvuygft"
    return ''.join([alphabet[((modinv(key[0], 26) * (alphabet.index(c) - key[1])) % 26)] for c in cipher if c in alphabet])

# Function to perform encryption or decryption based on the mode
def perform_custom_affine(text, key, mode):
    if mode == '1':
        return custom_affine_encrypt(text, key)
    elif mode == '2':
        return custom_affine_decrypt(text, key)
    else:
        return 'Pilihan tidak ada!'

# Driver Code to test the above functions
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
