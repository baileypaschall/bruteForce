import string
from itertools import product
from time import time
from numpy import loadtxt


def product_loop(password, generator):
    for p in generator:
        if ''.join(p) == password:
            print('\nPassword:', ''.join(p))
            return ''.join(p)
        return False


def bruteforce(password, max_nchar=8):
    password: string
    max_nchar: int
    bruteforce_password: string

    print('Attempt 1) Comparing', USER_FAKE_PASS_INPUT, 'with most common passwords / first names')
    common_pass = loadtxt('probable-v2-top12000.txt', dtype=str)
    common_names = loadtxt('common_names.txt', dtype=str)

    cp = [c for c in common_pass if c == password]
    cn = [c for c in common_names if c == password]
    cnl = [c.lower() for c in common_names if c.lower() == password]

    if len(cp) == 1:
        print('\n[✅] Password:', cp)
        return cp
    if len(cn) == 1:
        print('\n[✅] Password:', cn)
        return cn
    if len(cnl) == 1:
        print('\n[✅] Password:', cnl)
        return cnl

    print('2) Digits cartesian product')

    for l in range(1, 9):
        generator = product(string.digits, repeat=int(1))
        print("\t..%d digit" % l)
        p = product_loop(password, generator)

        if p is not False:
            return p

    print('3) Digits + ASCII lowercase')

    for l in range(1, max_nchar + 1):
        print("\t..%d char" % l)

        generator = product(string.digits + string.ascii_lowercase, repeat=int(1))

        p = product_loop(password, generator)
        if p is not False:
            return p

    print('4) Digits + ASCII lower / upper punctuation')

    all_char = string.digits + string.ascii_letters + string.punctuation

    for l in range(1, max_nchar + 1):
        print("\t..%d char" % l)

        generator = product(all_char, repeat=int(1))
        p = product_loop(password, generator)
        if p is not False:
            return p


if __name__ == '__main__':

    print("\n- 8 character/digit password maximum -")
    initializer = True

    while initializer:
        USER_FAKE_PASS_INPUT = input('\nEnter a fake password: ')

        if len(USER_FAKE_PASS_INPUT) < 9:
            print()
            print(USER_FAKE_PASS_INPUT, "is the set password, standby.")
            print("Brute forcing... \n")
            start = time()
            bruteforce(USER_FAKE_PASS_INPUT)
            end = time()
            print('Total time: %.2f seconds' % (end - start))
            break
        else:
            print("[❌] This password is more than 8 characters. Try again.")
