

def md4(message):

    def f(x, y, z):
        return (x & y) | (~x & z)

    def g(x, y, z):
        return (x & y) | (x & z) | (y & z)

    def h(x, y, z):
        return x ^ y ^ z

    mask = 0xFFFFFFFF

    a = 0x01234567
    b = 0x89ABCDEF
    c = 0xFEDCBA98
    d = 0x76543210

    message = bin(int.from_bytes(message.encode(), 'big'))[2:]
    bin_len = bin(len(message) - 1)[2:].zfill(64)
    message += '1'
    while len(message) % 512 != 448:
        message += '0'
    message += bin_len
    m = [message[x:x+16] for x in range(0, len(message), 16)]
    for mi in m:
        x = []
        for i in range(16):
            x.append(int('0b' + mi[i], 2))

        aa = a
        bb = b
        cc = c
        dd = d
        abcd = [a, b, c, d]

        s = [3, 7, 11, 19]
        for n in range(16):
            abcd[-n % 4] = ((abcd[-n % 4] + f(abcd[1 - n % 4], abcd[2 - n % 4], abcd[3 - n % 4]) + x[n])
                            << s[n % 4]) & mask

        xi = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]
        s = [3, 5, 9, 13]
        for n in range(16):
            abcd[-n % 4] = ((abcd[-n % 4] + g(abcd[1 - n % 4], abcd[2 - n % 4], abcd[3 - n % 4]) + x[xi[n]]
                            + 0x5A827999) << s[n % 4]) & mask

        xi = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        s = [3, 9, 11, 15]
        for n in range(16):
            abcd[-n % 4] = ((abcd[-n % 4] + h(abcd[1 - n % 4], abcd[2 - n % 4], abcd[3 - n % 4]) + x[xi[n]]
                            + 0x6ED9EBA1) << s[n % 4]) & mask

        a = (abcd[0] + aa) & mask
        b = (abcd[1] + bb) & mask
        c = (abcd[2] + cc) & mask
        d = (abcd[3] + dd) & mask

    hash_message = hex(int(bin(a) + bin(b)[2:] + bin(c)[2:] + bin(d)[2:], 2))

    return hash_message


print(md4('The quick brown fox jumps over the lazy dog'))
