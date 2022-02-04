import random, time
from typing import Text

__KEY_LENGTH__ = 8
__EXPONENT_KEY_LENGTH__ = 4
__BLOCK_LENGTH__ = 1
__ENCODE__ = 'utf-8'

def UpdateSeed():
    seed = int(time.time())
    random.seed(version=seed)

def IsPrime(number: int) -> bool:
    if (number == 2 or number == 3):
        return True
    if (number % 2 == 0 or number % 3 == 0 or number == 1):
        return False
    i = 5
    while (i*i < number):
        if (number % i == 0 or number % (i + 2) == 0):
            return False
        i += 4
    return True

def SplitString(text: str) -> tuple[str]:
    return [text[i:i+__BLOCK_LENGTH__] for i in range(0, len(text), __BLOCK_LENGTH__)]

def gcd(value1: int, value2: int) -> int:
    while ((value1 != 0) and (value2 != 0)):
        if (value1 > value2):
            value1 -= value2
        else:
            value2 -= value1
    return max(value1, value2)

def GetRandomPrimeNumber(exponent: bool = False) -> int:
    number = GenerateNumber(exponent)
    while not IsPrime(number):
        number = GenerateNumber(exponent)
    return number

def GenerateNumber(exponent: bool = False) -> int:
    if exponent: 
        length = __EXPONENT_KEY_LENGTH__ 
    else: 
        length = __KEY_LENGTH__
    return random.getrandbits(length)

def GetExponent(Euler: int) -> int:
    Exponent = GetRandomPrimeNumber(True)
    while Exponent > Euler or gcd(Exponent, Euler) != 1:
        Exponent = GetRandomPrimeNumber()
    return Exponent

def GetPrivateKey(Euler: int, Exponent: int) -> int:
    PrivateKey = GetRandomPrimeNumber()
    count = 0
    while (PrivateKey * Exponent) % Euler != 1:
        if count % 200 == 0: 
            UpdateSeed()
            Exponent = GetExponent(Euler)
        PrivateKey = GetRandomPrimeNumber()
        count += 1
    return PrivateKey

def GenerateKeys():
    UpdateSeed()
    FirstKey = 3 #GetRandomPrimeNumber()
    SecondKey = 7 #GetRandomPrimeNumber()
    PublicKey = FirstKey * SecondKey;
    Euler = (FirstKey - 1) * (SecondKey - 1)
    Exponent = GetExponent(Euler)
    PrivateKey = GetPrivateKey(Euler, Exponent)
    return (Exponent, PublicKey), (PrivateKey, PublicKey)

def Decode(text: str, pubkey: tuple[int, int]) -> str:
    blocks = SplitString(text)
    decodedblocks = []
    for block in blocks:
        value = int.from_bytes(bytes(block, __ENCODE__), byteorder='big', signed=True)
        print('blockdv: ', value)
        decodedblocks.append(pow(value, pubkey[0], pubkey[1]))
    return ' '.join(str(block) for block in decodedblocks)

def Encode(text: int, privkey: tuple[int, int]) -> str:
    decodedblocks = text.split(' ')
    blocks = []
    for block in decodedblocks:
        value = pow(int(block), privkey[0], privkey[1])
        print('blockdc', value)
        blocks.append(value.to_bytes(value.bit_length(), byteorder='big', signed=True))
    return b''.join(block for block in blocks)

def Main() -> None:
    pubkey, privkey = GenerateKeys()
    while True:
        text = input(' > ')
        decoded = Decode(text, pubkey)
        print('decoded: ', decoded)
        encoded = Encode(decoded, privkey)
        print('encoded: ', encoded.decode(__ENCODE__))

if __name__ == "__main__":
    try:
        Main()
    except KeyboardInterrupt:
        exit('User close program')
