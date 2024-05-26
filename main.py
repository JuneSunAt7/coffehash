import hashlib
from colorama import Fore, Style

def create_md5_hash_string(input_string):
    hash_object = hashlib.md5(input_string.encode())
    hash_string = hash_object.hexdigest()
    return hash_string

def unhash_md5_string(pathToWordlist, hashedstring):
    # Чтение списка слов из файла
    with open(pathToWordlist, 'r') as file:
        wordlist = file.read().splitlines()
    for word in wordlist:
        if hashlib.md5(word.encode()).hexdigest() == hashedstring:
            print(Fore.GREEN + f"Найдено совпадение: {word}" + Style.RESET_ALL)

input_string = "Hello, World!"
hash_string = create_md5_hash_string(input_string)
print(Fore.CYAN + "md5 hash " + hash_string+ Style.RESET_ALL)
unhash_md5_string("wordlist.txt", hash_string)