import hashlib
import os
import base64


class PasswordHelper:
    def get_hash(self, plain):
        message = plain.encode()
        return hashlib.sha512(message).hexdigest()

    def get_salt(self):
        return base64.b64encode(os.urandom(20))

    def validate_password(self, plain, expected):
        return self.get_hash(plain)[:len(expected)] == expected
