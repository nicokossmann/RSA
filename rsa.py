import random

def check_prim(num):
    num = int(num)
    if num > 1:
        for i in range(2, num):
            if (num%i)==0:
                return False
            else:
                return True
    else:
        return False

def euclid(a, b):
    if a == 0:
        return b
    return euclid(b%a, a)

def extended_euclid(a, b):
    if a == 0:
        return (b, 0, 1)
    gcd, y, x = extended_euclid(b%a,a)
    return (gcd, x - (b//a) * y, y)

def mod_inverse(a, b):
    gcd, x, y = extended_euclid(a, b)
    if gcd != 1:
        raise Exception("Keine multiplikative Inverse gefunden!")
    return x%b

def get_random_gcd(phi):
    e = random.randrange(2, phi)
    while(euclid(e, phi) != 1):
        e = random.randrange(2, phi)
    return e 

def create_keys(p, q):
    N = p*q
    phi = (p-1)*(q-1)
    e  = get_random_gcd(phi)
    d = mod_inverse(e, phi)
    return ((e, N), (d, N))

def encrypt(m, e, N):
    return (m**e)%N

def decrypt(c, d, N):
    return (c**d)%N

def main():
    try:
        print("\nWILLKOMMEN ZUM RSA VER-/ENTSCHLÜSSELUNGS-TOOL")
        print("---------------------------------------------\n")
        p = int(input("Geben Sie eine Primzahl 'p' an: "))
        q = int(input("Geben sie eine Primzahl 'q' an: "))
        if check_prim(p) and check_prim(q):
            public_key, private_key = create_keys(p, q)
            print("\nPublic-Key: {}\nPrivate-Key: {}\n".format(public_key, private_key))
            e, N = public_key
            d, N = private_key
            choose = input("Geben Sie 'enc' zum Verschlüsseln und 'dec' zum Entschlüsseln der Nachricht an oder 'exit' zum beenden: ")
            while(choose != 'exit'):
                if choose == 'enc':
                    m = int(input("Geben Sie eine Nachricht 'm' an: "))
                    c = encrypt(m, e, N)
                    print("\nChiffre 'c' lautet: {}\n".format(c))
                elif choose == 'dec':
                    c = int(input("Geben Sie eine Chiffre 'c' an: "))
                    m = decrypt(c, d, N)
                    print("\nNachricht 'm' lautet: {}\n".format(m))
                else:
                    print("\nFalsche Eingabe!\n")
                choose = input("Geben Sie 'enc' zum Verschlüsseln und 'dec' zum Entschüsseln der Nachricht an oder 'exit' zum beenden: ")
        else:
            print("\n'p' oder 'q' sind keine Primzahl!\n")
        print("\n")
    except ValueError:
        print('\nKein Integer!\n')
        return
    
if __name__ == "__main__":
    main()
