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
    g, x, y = extended_euclid(a, b)
    if g != 1:
        raise Exception("Keine multiplikative Inverse")
    return x%b

def get_random_gcd(phi):
    e = random.randrange(2, phi)
    while(euclid(e, phi) != 1):
        e = random.randrange(2, phi)
    return e

def create_keys(p, q):
    n = p*q
    phi = (p-1)*(q-1)
    e  = get_random_gcd(phi)
    #e = 23
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(m, e, n):
    return (m**e)%n

def decrypt(c, d, n):
    return (c**d)%n

def main():
    print("\nWILLKOMMEN ZUM RSA VER-/ENTSCHLÜSSELUNGS-TOOL")
    print("---------------------------------------------\n")
    try:
       p = int(input("Geben Sie eine Primzahl 'p' an: "))
       q = int(input("Geben sie eine Primzahl 'q' an: "))
    except ValueError:
          print('Eingabe kein Integer\n')
          return
    if check_prim(p) and check_prim(q):
        public_key, private_key = create_keys(p, q)
        print("\nPublic Key: {}\nPrivate-Key: {}\n".format(public_key, private_key))
        e, n = public_key
        d, n = private_key
        choose = input("Geben Sie 'enc' zum Verschlüsseln und 'dec' zum Entschlüsseln der Nachricht an oder 'exit' zum beenden: ")
        while(choose != 'exit'):
            if choose == 'enc':
                m = int(input("Geben Sie eine Nachricht 'm' an: "))
                c = encrypt(m, e, n)
                print("\nChiffre 'c' lautet: {}\n".format(c))
            elif choose == 'dec':
                c = int(input("Geben Sie eine Chiffre 'c' an: "))
                m = decrypt(c, d, n)
                print("\nNachricht 'm' lautet: {}\n".format(m))
            else:
                print("Falsche Eingabe!")
            choose = input("Geben Sie 'enc' zum Verschlüsseln und 'dec' zum Entschüsseln der Nachricht an oder 'exit' zum beenden: ")
    else:
        print("'p' oder 'q' sind keine Primzahl!")
    print("\n")
    
if __name__ == "__main__":
    main()
