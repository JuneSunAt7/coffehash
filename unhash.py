import hashlib
from colorama import Fore, Style

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