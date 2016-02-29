def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return -1  # modular inverse does not exist
    else:
        return x % m


message = 'jkjdsdxc d eerefds'
key1 = 3
key2 = 7
mode = 'decrypt'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''
message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = ((num*key1)+key2)%26
        elif mode == 'decrypt':
            key1 = modinv(key1,26)
            num = (key1*(num-key2))%26
        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol
print (translated)