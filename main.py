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


input_string = "Hello, World!"
hash_string = create_md5_hash_string(input_string)
print(Fore.CYAN + "md5 hash " + hash_string+ Style.RESET_ALL)
unhash_md5_string("wordlist.txt", hash_string)

string_to_encode = "Hello, World!"
encoded_string = create_sha1_hash_string(string_to_encode)
print(Fore.CYAN +"Sha1 hash:", encoded_string+ Style.RESET_ALL)
unhash_sha1_string("wordlist.txt", encoded_string)

sha256_string =  "Hello, World!"
encoded_sha256 = create_sha256_hash_string(sha256_string)
print(Fore.CYAN + "Sha256 hash: " + encoded_sha256+ Style.RESET_ALL)
unhash_sha256_string("wordlist.txt", encoded_sha256)