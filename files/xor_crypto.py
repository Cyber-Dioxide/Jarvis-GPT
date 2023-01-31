
def BinaryToString(binary):
    decimal = int(binary, 2)
    return chr(decimal)


Message = input("Enter Message: ")
Key = input('Enter Key: ')

assert len(Key) == len(Message)

BinaryMessage = "".join(format(ord(i), '08b') for i in Message)
BinaryKey = "".join(format(ord(i), '08b') for i in Key)

XOR = bin(int(BinaryMessage, 2) ^ int(BinaryKey))[2:]

CIPHER = "0" * (len(BinaryKey) - len(XOR)) + XOR

CIPHER_LIST = []

for i in range(0, len(CIPHER), 8):
    CIPHER_LIST.append(CIPHER[i:i + 8])
    # sys.stdout.write(" " + CIPHER[i:i + 8])
print(CIPHER_LIST)

STRING = "".join(list(map(BinaryToString, CIPHER_LIST)))
print(STRING.format('utf-8'))
