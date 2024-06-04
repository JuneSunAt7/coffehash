import hashlib
from colorama import Fore, Style


def create_md5_hash_string(input_string):
    hash_object = hashlib.md5(input_string.encode())
    hash_string = hash_object.hexdigest()
    return hash_string


def create_sha1_hash_string(input_string):
    sha1 = hashlib.sha1()
    sha1.update(input_string.encode('utf-8'))
    return sha1.hexdigest()


def create_sha256_hash_string(input_sttring):
    sha256 = hashlib.sha256()
    sha256.update(input_string.encode('utf-8'))
    return sha256.hexdigest()


def create_sha512_hash_string(input_string):
    sha512 = hashlib.sha512()
    sha512.update(input_string.encode('utf-8'))
    return sha512.hexdigest()

def unhash_md5_string(pathToWordlist, hashedstring):
    # Чтение списка слов из файла
    with open(pathToWordlist, 'r') as file:
        wordlist = file.read().splitlines()
    for word in wordlist:
        if hashlib.md5(word.encode()).hexdigest() == hashedstring:
            print(Fore.GREEN + f"Найдено совпадение: {word}" + Style.RESET_ALL)


def unhash_sha1_string(pathToWordlist, hashedstring):
    with open(pathToWordlist, 'r') as file:
        wordlist = file.read().splitlines()
    for word in wordlist:
        if hashlib.sha1(word.encode()).hexdigest() == hashedstring:
            print(Fore.GREEN + f"Найдено совпадение: {word}" + Style.RESET_ALL)

def unhash_sha256_string(pathToWordlist, hashedstring):
    with open(pathToWordlist, 'r') as file:
        wordlist = file.read().splitlines()
    for word in wordlist:
        if hashlib.sha256(word.encode()).hexdigest() == hashedstring:
            print(Fore.GREEN + f"Найдено совпадение: {word}" + Style.RESET_ALL)


def unhash_sha512_string(pathToWordlist, hashedstring):
    with open(pathToWordlist, 'r') as file:
        wordlist = file.read().splitlines()
    for word in wordlist:
        if hashlib.sha512(word.encode()).hexdigest() == hashedstring:
            print(Fore.GREEN + f"Найдено совпадение: {word}" + Style.RESET_ALL)


import sys


def main(algorithm, hash, wordlist):
   if algorithm == "md5":
        unhash_md5_string(wordlist, hash)
   elif algorithm == "sha1":
       unhash_sha1_string(wordlist, hash)
   elif algorithm == "sha256":
       unhash_sha256_string(wordlist, hash)
   elif algorithm == "sha512":
       unhash_sha512_string(wordlist, hash)
   else:
       print(Fore.RED + "Unable algorithm"+ Style.RESET_ALL)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(Fore.MAGENTA + "Usage: python main.py 'algorithm' 'hash' 'wordlist'")
        sys.exit(1)

    alg = sys.argv[1]
    hash = sys.argv[2]
    wlist = sys.argv[3]

    main(alg, hash, wlist)


