import os
from os import chmod
from Crypto.PublicKey import RSA

class GenerateSSHKey():
    def __init__(self, user):
        self.user = user
        self.dir = '/tmp/sshkeys/'
        self.location = self.dir + self.user
        self.key = RSA.generate(2048)
        self.ext = (".key")
 
    def PrivateKey(self):
        self.t = "_private"
        self.file = self.location + self.t + self.ext
        if not os.path.exists(self.location):
            try:
                os.makedirs(self.location)
            except OSError as exception:
                if exception.errno != errno.EEXIST:
                    raise
        with open(self.file, 'w') as content_file:
          chmod(self.file, 0600)
          content_file.write(self.key.exportKey('PEM'))
        return self.file
 
    def PublicKey(self):
        self.pubkey = self.key.publickey()
        self.t = "_public"
        self.file = self.location + self.t + self.ext
        if not os.path.exists(self.location):
            try:
                os.makedirs(self.location)
            except OSError as exception:
                if exception.errno != errno.EEXIST:
                    raise 
        with open(self.file, 'w') as content_file:
          content_file.write(self.pubkey.exportKey('OpenSSH'))
        return self.file

user = "myusername"
Gen = GenerateSSHKey(user)
print Gen.PrivateKey() 
print Gen.PublicKey() 
