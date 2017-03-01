
import requests
from simplecrypt import decrypt

code = requests.get('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').content
passes = requests.get('https://stepic.org/media/attachments/lesson/24466/passwords.txt').content

for p in passes.split():
        s = decrypt(p, code)
        print(p, s)
