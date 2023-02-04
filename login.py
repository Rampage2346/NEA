import pandas as pd

creds = pd.read_csv("creds.csv")

characters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def sha1(data):
    bytes = ""

    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    for n in range(len(data)):
        bytes += '{0:08b}'.format(ord(data[n]))
    bits = bytes + "1"
    pBits = bits

    while len(pBits) % 512 != 448:
        pBits += "0"

    pBits += '{0:064b}'.format(len(bits) - 1)

    def chunks(l, n):
        return [l[i:i + n] for i in range(0, len(l), n)]

    def rol(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff

    for c in chunks(pBits, 512):
        words = chunks(c, 32)
        w = [0] * 80
        for n in range(0, 16):
            w[n] = int(words[n], 2)
        for i in range(16, 80):
            w[i] = rol((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = rol(a, 5) + f + e + k + w[i] & 0xffffffff
            e = d
            d = c
            c = rol(b, 30)
            b = a
            a = temp

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)


def checkPass(inpuser, inppass):
    accept = False
    creds = pd.read_csv("creds.csv")

    is_correct_user = (creds['username'] == sha1(inpuser))
    # print(is_correct_user)
    is_correct_pass = (creds['password'] == sha1(inppass))
    # print(is_correct_pass)

    for i in range(0, len(creds)):
        if is_correct_user[i]:
            user = True
            break
    else:
        user = False

    for i in range(0, len(creds)):
        if is_correct_pass[i]:
            passw = True
            break
    else:
        passw = False

    if user == True and passw == True:
        accept = True

    return accept


def addUser(userN, userP):
    data = {
        'username': [sha1(userN)],
        'password': [sha1(userP)],
    }
    df = pd.DataFrame(data)
    df.to_csv('creds.csv', mode='a', index=False, header=False)
    print("Data appended successfully.")


def new_user_append(inpuser, inppass):
    numbers = [
        '1', '2', '3', '4', '5',
        '6', '7', '8', '9', '0'
    ]
    usern = [*inpuser]
    passw = [*inppass]

    for i in range(0, len(usern)):
        if usern[i] in numbers:
            tempusern = chr((int((usern[i]))) + 64)
            print(tempusern)
            usern[i] = str(tempusern)

    for i in range(0, len(passw)):
        if passw[i] in numbers:
            temppassw = chr((int((passw[i]))) + 64)

            passw[i] = str(temppassw)

    print(usern)
    print(passw)
    inpuser = "".join(usern)
    inppass = "".join(passw)
    print(inpuser, inppass)
    print(type(inpuser), type(inppass))

    addUser(inpuser, inppass)


def login_cred_check(inpuser, inppass):
    numbers = [
        '1', '2', '3', '4', '5',
        '6', '7', '8', '9', '0'
    ]
    usern = [*inpuser]
    passw = [*inppass]

    for i in range(0, len(usern)):
        if usern[i] in numbers:
            tempusern = chr((int((usern[i]))) + 64)
            print(tempusern)
            usern[i] = str(tempusern)

    for i in range(0, len(passw)):
        if passw[i] in numbers:
            temppassw = chr((int((passw[i]))) + 64)

            passw[i] = str(temppassw)

    print(usern)
    print(passw)
    inpuser = "".join(usern)
    inppass = "".join(passw)
    print(inpuser, inppass)
    print(type(inpuser), type(inppass))

    check = checkPass(inpuser, inppass)
    return check


def mainLogin():
    add = input("Login or Add New User: L/A\n\t")

    if add == "L":
        logged_in = login_no_hash()
        print(logged_in)
    elif add == "A":
        newuser = input("Enter your new username\n\t")
        newpass = input("Enter your new password\n\t")
        addUser(newuser, newpass)

    print("-----")
    df = pd.read_csv('creds.csv')
    print(df.to_string())


def login_no_hash():
    inpuser = input("Enter your username\n\t")
    inppass = input("Enter you password\n\t")
    check = checkPass(inpuser, inppass)
    return check

# mainLogin()
